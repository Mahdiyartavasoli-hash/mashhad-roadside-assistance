from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import BlogPost, FAQ, SEOSettings, Service, SiteSettings, Stat, Testimonial, VehicleCategory


class Command(BaseCommand):
    help = 'Create safe demo content for local development.'

    def handle(self, *args, **options):
        SiteSettings.objects.update_or_create(pk=1, defaults={'brand_name_fa':'امداد خودرو مشهد','brand_name_en':'Mashhad Roadside Assistance','phone':'09120000000','whatsapp':'989120000000','tagline_fa':'امداد خودرو مشهد، ۲۴ ساعته کنار شما','tagline_en':'24/7 roadside assistance across Mashhad'})
        SEOSettings.objects.update_or_create(pk=1, defaults={'meta_title_fa':'امداد خودرو مشهد | امداد خودرو ۲۴ ساعته','meta_title_en':'Mashhad Roadside Assistance | 24/7','meta_description_fa':'امداد خودرو ۲۴ ساعته در مشهد؛ یدک‌کش، خودروبر، مکانیک سیار، امداد باتری و خدمات خودرو در محل.','meta_description_en':'24/7 roadside assistance in Mashhad including towing, mobile mechanic, battery and vehicle recovery.'})
        services = [
            ('towing','یدک‌کش','Towing','حمل ایمن خودرو در سراسر مشهد.','Safe vehicle towing across Mashhad.','truck',1),
            ('vehicle-recovery','خودروبر','Vehicle Recovery','حمل خودروهای خراب یا تصادفی.','Recovery for broken-down or accident vehicles.','truck',2),
            ('mobile-mechanic','مکانیک سیار','Mobile Mechanic','تعمیر و عیب‌یابی خودرو در محل.','On-site vehicle repair and diagnostics.','wrench',3),
            ('battery','امداد باتری','Battery Assistance','باتری به باتری و خدمات باتری در محل.','Jump-start and battery assistance on site.','battery',4),
            ('tire','پنچرگیری سیار','Mobile Tire Service','پنچرگیری و تعویض لاستیک در محل.','Mobile tire repair and replacement.','tire',5),
            ('fuel','سوخت‌رسانی سیار','Mobile Fuel Delivery','رساندن سوخت در شرایط اضطراری.','Emergency fuel delivery.','fuel',6),
            ('electrical','برق خودرو','Auto Electrical','عیب‌یابی و تعمیر برق خودرو.','Vehicle electrical diagnostics and repair.','bolt',7),
            ('lockout','باز کردن درب خودرو','Vehicle Lockout','کمک در شرایط قفل شدن خودرو.','Help when you are locked out of your vehicle.','key',8),
        ]
        for slug, fa, en, dfa, den, icon, order in services:
            Service.objects.update_or_create(slug=slug, defaults={'title_fa':fa,'title_en':en,'description_fa':dfa,'description_en':den,'icon':icon,'sort_order':order,'enabled':True})
        vehicles = [
            ('iran-khodro','ایران خودرو','Iran Khodro','پژو، سمند، دنا، تارا و سایر مدل‌ها.','Peugeot, Samand, Dena, Tara and more.','پژو\nسمند\nدنا\nتارا','Peugeot\nSamand\nDena\nTara',1),
            ('saipa','سایپا','Saipa','پراید، تیبا، شاهین، کوییک و سایر مدل‌ها.','Pride, Tiba, Shahin, Quick and more.','پراید\nتیبا\nشاهین\nکوییک','Pride\nTiba\nShahin\nQuick',2),
            ('chinese','خودروهای چینی','Chinese Vehicles','انواع خودروهای چینی موجود در بازار ایران.','Popular Chinese vehicles in Iran.','','',3),
            ('foreign','خودروهای خارجی','Foreign Vehicles','خودروهای خارجی و لوکس.','Foreign and luxury vehicles.','تویوتا\nهیوندای\nکیا\nBMW\nMercedes','Toyota\nHyundai\nKia\nBMW\nMercedes',4),
        ]
        for row in vehicles:
            VehicleCategory.objects.update_or_create(slug=row[0], defaults={'title_fa':row[1],'title_en':row[2],'description_fa':row[3],'description_en':row[4],'models_fa':row[5],'models_en':row[6],'sort_order':row[7],'enabled':True})
        for fa, en, value, order in [('مأموریت موفق','Successful missions','+5000',1),('پاسخگویی','Availability','24/7',2),('سال تجربه','Years of experience','+10',3),('رضایت مشتری','Customer satisfaction','98%',4)]:
            Stat.objects.update_or_create(value=value, defaults={'label_fa':fa,'label_en':en,'sort_order':order,'enabled':True})
        faqs = [
            ('آیا امداد خودرو ۲۴ ساعته است؟','Is roadside assistance available 24/7?','بله، خدمات برای پاسخگویی شبانه‌روزی طراحی شده است.','Yes, the service is designed for 24/7 assistance.',1),
            ('چه مناطقی از مشهد را پوشش می‌دهید؟','Which areas of Mashhad do you cover?','هدف سرویس، پوشش سراسر مشهد است.','The service is intended to cover Mashhad citywide.',2),
            ('آیا مکانیک به محل اعزام می‌شود؟','Can a mechanic come to my location?','بله، برای مشکلات قابل تعمیر در محل، مکانیک سیار اعزام می‌شود.','Yes, a mobile mechanic can be dispatched for on-site repairs.',3),
        ]
        for qfa,qen,afa,aen,order in faqs:
            FAQ.objects.update_or_create(question_fa=qfa, defaults={'question_en':qen,'answer_fa':afa,'answer_en':aen,'sort_order':order,'enabled':True})
        if not Testimonial.objects.exists():
            Testimonial.objects.bulk_create([Testimonial(name='مشتری نمونه',text_fa='این متن نمونه است و قبل از انتشار باید با نظر واقعی مشتری جایگزین شود.',text_en='Demo text. Replace this with a real customer review before publishing.',rating=5,sort_order=1),Testimonial(name='مشتری نمونه ۲',text_fa='این متن نمونه است و قبل از انتشار باید با نظر واقعی مشتری جایگزین شود.',text_en='Demo text. Replace this with a real customer review before publishing.',rating=5,sort_order=2)])
        if not BlogPost.objects.exists():
            BlogPost.objects.create(slug='car-wont-start',title_fa='وقتی ماشین روشن نمی‌شود چه کار کنیم؟',title_en='What to Do When Your Car Will Not Start',excerpt_fa='چند بررسی ساده که قبل از درخواست امداد خودرو می‌توانید انجام دهید.',excerpt_en='A few simple checks you can make before requesting roadside assistance.',content_fa='این مقاله محتوای نمونه برای توسعه محلی است. قبل از انتشار، محتوای تخصصی نهایی را جایگزین کنید.',content_en='This is demo content for local development. Replace it with the final expert article before publishing.',meta_title_fa='وقتی ماشین روشن نمی‌شود چه کنیم؟',meta_title_en='What to Do When Your Car Will Not Start',published=True,published_at=timezone.now())
        self.stdout.write(self.style.SUCCESS('Demo content created/updated successfully.'))
