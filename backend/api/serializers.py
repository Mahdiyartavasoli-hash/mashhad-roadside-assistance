from django.utils.html import strip_tags
from rest_framework import serializers
from core.models import (
    BlogPost, FAQ, Lead, SEOSettings, Service, SiteSettings, Stat,
    Testimonial, VehicleCategory,
)


class AbsoluteMediaMixin:
    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        if request:
            for key, value in list(data.items()):
                if isinstance(value, str) and value.startswith('/media/'):
                    data[key] = request.build_absolute_uri(value)
        return data


class SiteSettingsSerializer(AbsoluteMediaMixin, serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = '__all__'


class SEOSettingsSerializer(AbsoluteMediaMixin, serializers.ModelSerializer):
    class Meta:
        model = SEOSettings
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class VehicleCategorySerializer(serializers.ModelSerializer):
    models_fa_list = serializers.SerializerMethodField()
    models_en_list = serializers.SerializerMethodField()

    class Meta:
        model = VehicleCategory
        fields = '__all__'
        extra_fields = ('models_fa_list', 'models_en_list')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['models_fa_list'] = [x.strip() for x in instance.models_fa.splitlines() if x.strip()]
        data['models_en_list'] = [x.strip() for x in instance.models_en.splitlines() if x.strip()]
        return data

    def get_models_fa_list(self, obj):
        return [x.strip() for x in obj.models_fa.splitlines() if x.strip()]

    def get_models_en_list(self, obj):
        return [x.strip() for x in obj.models_en.splitlines() if x.strip()]


class BlogPostSerializer(AbsoluteMediaMixin, serializers.ModelSerializer):
    content_fa_text = serializers.SerializerMethodField()
    content_en_text = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = '__all__'

    def get_content_fa_text(self, obj):
        return strip_tags(obj.content_fa)

    def get_content_en_text(self, obj):
        return strip_tags(obj.content_en)


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'phone', 'vehicle', 'problem', 'location', 'description', 'website', 'created_at')
        read_only_fields = ('id', 'created_at')

    def validate_website(self, value):
        if value.strip():
            raise serializers.ValidationError('Invalid submission.')
        return ''

    def validate_name(self, value):
        value = ' '.join(value.split())
        if len(value) < 2:
            raise serializers.ValidationError('نام واردشده معتبر نیست.')
        return value

    def validate_phone(self, value):
        cleaned = ''.join(ch for ch in value if ch.isdigit() or ch == '+')
        digits = cleaned.replace('+', '')
        if len(digits) < 8 or len(digits) > 15:
            raise serializers.ValidationError('شماره تماس معتبر نیست.')
        return cleaned

    def validate_location(self, value):
        value = value.strip()
        if len(value) < 3:
            raise serializers.ValidationError('لطفاً موقعیت یا آدرس را وارد کنید.')
        return value

    def validate_description(self, value):
        if len(value) > 2000:
            raise serializers.ValidationError('توضیحات بیش از حد طولانی است.')
        return value.strip()
