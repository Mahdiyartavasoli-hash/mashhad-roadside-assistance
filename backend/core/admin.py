from django.contrib import admin
from django.utils import timezone
from .models import (
    BlogPost, FAQ, Lead, SEOSettings, Service, SiteSettings, Stat,
    Testimonial, VehicleCategory,
)


admin.site.site_header = 'مدیریت امداد خودرو مشهد'
admin.site.site_title = 'CMS امداد خودرو'
admin.site.index_title = 'مدیریت محتوای سایت'


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('برند و تماس', {'fields': ('brand_name_fa', 'brand_name_en', 'phone', 'whatsapp')}),
        ('محتوا', {'fields': ('tagline_fa', 'tagline_en', 'description_fa', 'description_en', 'city_fa', 'city_en', 'working_hours')}),
        ('رسانه', {'fields': ('logo', 'hero_image')}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()


@admin.register(SEOSettings)
class SEOSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Meta', {'fields': ('meta_title_fa', 'meta_title_en', 'meta_description_fa', 'meta_description_en')}),
        ('Sharing & Canonical', {'fields': ('og_image', 'canonical_url')}),
    )

    def has_add_permission(self, request):
        return not SEOSettings.objects.exists()


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title_fa', 'slug', 'enabled', 'sort_order', 'updated_at')
    list_editable = ('enabled', 'sort_order')
    list_filter = ('enabled',)
    prepopulated_fields = {'slug': ('title_en',)}
    search_fields = ('title_fa', 'title_en', 'description_fa', 'description_en')
    ordering = ('sort_order', 'id')


@admin.register(VehicleCategory)
class VehicleCategoryAdmin(admin.ModelAdmin):
    list_display = ('title_fa', 'slug', 'enabled', 'sort_order')
    list_editable = ('enabled', 'sort_order')
    list_filter = ('enabled',)
    prepopulated_fields = {'slug': ('title_en',)}
    search_fields = ('title_fa', 'title_en', 'models_fa', 'models_en')


@admin.action(description='انتشار مقالات انتخاب‌شده')
def publish_posts(modeladmin, request, queryset):
    queryset.update(published=True, published_at=timezone.now())


@admin.action(description='لغو انتشار مقالات انتخاب‌شده')
def unpublish_posts(modeladmin, request, queryset):
    queryset.update(published=False)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title_fa', 'published', 'published_at', 'updated_at')
    list_filter = ('published', 'published_at')
    search_fields = ('title_fa', 'title_en', 'excerpt_fa', 'excerpt_en')
    prepopulated_fields = {'slug': ('title_en',)}
    date_hierarchy = 'published_at'
    actions = (publish_posts, unpublish_posts)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question_fa', 'enabled', 'sort_order')
    list_editable = ('enabled', 'sort_order')
    list_filter = ('enabled',)
    search_fields = ('question_fa', 'question_en', 'answer_fa', 'answer_en')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'enabled', 'sort_order')
    list_editable = ('rating', 'enabled', 'sort_order')
    list_filter = ('enabled', 'rating')
    search_fields = ('name', 'text_fa', 'text_en')


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('label_fa', 'value', 'enabled', 'sort_order')
    list_editable = ('value', 'enabled', 'sort_order')
    list_filter = ('enabled',)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'problem', 'status', 'created_at')
    list_filter = ('status', 'problem', 'created_at')
    search_fields = ('name', 'phone', 'vehicle', 'location', 'description')
    readonly_fields = ('created_at', 'updated_at')
    exclude = ('website',)
    date_hierarchy = 'created_at'
    list_per_page = 50
