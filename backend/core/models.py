from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SiteSettings(TimeStampedModel):
    brand_name_fa = models.CharField(max_length=120, default='امداد خودرو مشهد')
    brand_name_en = models.CharField(max_length=120, default='Mashhad Roadside Assistance')
    phone = models.CharField(max_length=30, default='09120000000')
    whatsapp = models.CharField(max_length=30, blank=True)
    tagline_fa = models.CharField(max_length=255, default='امداد خودرو مشهد، ۲۴ ساعته کنار شما')
    tagline_en = models.CharField(max_length=255, default='24/7 roadside assistance across Mashhad')
    description_fa = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    city_fa = models.CharField(max_length=80, default='مشهد')
    city_en = models.CharField(max_length=80, default='Mashhad')
    working_hours = models.CharField(max_length=80, default='24/7')
    logo = models.ImageField(upload_to='branding/', blank=True, null=True)
    hero_image = models.ImageField(upload_to='branding/', blank=True, null=True)

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class SEOSettings(TimeStampedModel):
    meta_title_fa = models.CharField(max_length=70, default='امداد خودرو مشهد | امداد خودرو ۲۴ ساعته')
    meta_title_en = models.CharField(max_length=70, default='Mashhad Roadside Assistance | 24/7')
    meta_description_fa = models.CharField(max_length=170, blank=True)
    meta_description_en = models.CharField(max_length=170, blank=True)
    og_image = models.ImageField(upload_to='seo/', blank=True, null=True)
    canonical_url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'تنظیمات SEO'
        verbose_name_plural = 'تنظیمات SEO'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class Service(TimeStampedModel):
    slug = models.SlugField(max_length=100, unique=True)
    title_fa = models.CharField(max_length=120)
    title_en = models.CharField(max_length=120)
    description_fa = models.TextField()
    description_en = models.TextField()
    icon = models.CharField(max_length=50, default='wrench')
    sort_order = models.PositiveIntegerField(default=0)
    enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ['sort_order', 'id']


class VehicleCategory(TimeStampedModel):
    slug = models.SlugField(max_length=100, unique=True)
    title_fa = models.CharField(max_length=120)
    title_en = models.CharField(max_length=120)
    description_fa = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    models_fa = models.TextField(blank=True, help_text='مدل‌ها را با خط جدید جدا کنید.')
    models_en = models.TextField(blank=True, help_text='One model per line.')
    sort_order = models.PositiveIntegerField(default=0)
    enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ['sort_order', 'id']


class BlogPost(TimeStampedModel):
    slug = models.SlugField(max_length=180, unique=True)
    title_fa = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    excerpt_fa = models.TextField()
    excerpt_en = models.TextField()
    content_fa = models.TextField()
    content_en = models.TextField()
    cover_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    meta_title_fa = models.CharField(max_length=70, blank=True)
    meta_title_en = models.CharField(max_length=70, blank=True)
    meta_description_fa = models.CharField(max_length=170, blank=True)
    meta_description_en = models.CharField(max_length=170, blank=True)
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['published', '-published_at']),
            models.Index(fields=['slug']),
        ]


class FAQ(TimeStampedModel):
    question_fa = models.CharField(max_length=300)
    question_en = models.CharField(max_length=300)
    answer_fa = models.TextField()
    answer_en = models.TextField()
    sort_order = models.PositiveIntegerField(default=0)
    enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ['sort_order', 'id']


class Testimonial(TimeStampedModel):
    name = models.CharField(max_length=120)
    text_fa = models.TextField()
    text_en = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    enabled = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']


class Stat(TimeStampedModel):
    label_fa = models.CharField(max_length=120)
    label_en = models.CharField(max_length=120)
    value = models.CharField(max_length=30)
    sort_order = models.PositiveIntegerField(default=0)
    enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ['sort_order', 'id']


class Lead(TimeStampedModel):
    class Problem(models.TextChoices):
        TOWING = 'towing', 'یدک‌کش / خودروبر'
        BATTERY = 'battery', 'باتری'
        FLAT_TIRE = 'flat_tire', 'پنچری'
        MECHANIC = 'mechanic', 'مکانیک سیار'
        FUEL = 'fuel', 'سوخت‌رسانی'
        LOCKOUT = 'lockout', 'قفل / کلید'
        ELECTRICAL = 'electrical', 'برق خودرو'
        ACCIDENT = 'accident', 'تصادف'
        OTHER = 'other', 'سایر'

    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    vehicle = models.CharField(max_length=120, blank=True)
    problem = models.CharField(max_length=30, choices=Problem.choices, default=Problem.OTHER)
    location = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=30, default='new', choices=[
        ('new', 'جدید'),
        ('contacted', 'تماس گرفته شد'),
        ('in_progress', 'در حال پیگیری'),
        ('completed', 'تکمیل شد'),
        ('cancelled', 'لغو شد'),
    ])
    website = models.CharField(max_length=120, blank=True, help_text='Spam honeypot. Should remain empty.')

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status', '-created_at']),
            models.Index(fields=['phone']),
        ]
