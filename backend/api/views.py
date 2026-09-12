from django.http import JsonResponse
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView

from core.models import (
    BlogPost, FAQ, Lead, SEOSettings, Service, SiteSettings, Stat,
    Testimonial, VehicleCategory,
)
from .serializers import (
    BlogPostSerializer, FAQSerializer, LeadSerializer, SEOSettingsSerializer,
    ServiceSerializer, SiteSettingsSerializer, StatSerializer,
    TestimonialSerializer, VehicleCategorySerializer,
)


class PublicReadThrottle(AnonRateThrottle):
    rate = '120/min'


class LeadCreateThrottle(AnonRateThrottle):
    rate = '10/hour'


class SiteDataView(APIView):
    """Return only published/public content required by the frontend."""
    permission_classes = [AllowAny]
    throttle_classes = [PublicReadThrottle]

    def get(self, request):
        site = SiteSettings.objects.first()
        seo = SEOSettings.objects.first()
        return Response({
            'site': SiteSettingsSerializer(site, context={'request': request}).data if site else None,
            'seo': SEOSettingsSerializer(seo, context={'request': request}).data if seo else None,
            'services': ServiceSerializer(Service.objects.filter(enabled=True), many=True, context={'request': request}).data,
            'vehicles': VehicleCategorySerializer(VehicleCategory.objects.filter(enabled=True), many=True, context={'request': request}).data,
            'blog': BlogPostSerializer(BlogPost.objects.filter(published=True, published_at__lte=timezone.now())[:6], many=True, context={'request': request}).data,
            'faq': FAQSerializer(FAQ.objects.filter(enabled=True), many=True).data,
            'testimonials': TestimonialSerializer(Testimonial.objects.filter(enabled=True), many=True).data,
            'stats': StatSerializer(Stat.objects.filter(enabled=True), many=True).data,
        })


class LeadCreateView(generics.CreateAPIView):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    permission_classes = [AllowAny]
    throttle_classes = [LeadCreateThrottle]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {'success': True, 'message': 'درخواست شما با موفقیت ثبت شد.'},
            status=status.HTTP_201_CREATED,
        )


class BlogListView(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]
    throttle_classes = [PublicReadThrottle]

    def get_queryset(self):
        return BlogPost.objects.filter(
            published=True,
            published_at__lte=timezone.now(),
        ).order_by('-published_at')


class BlogDetailView(generics.RetrieveAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]
    throttle_classes = [PublicReadThrottle]
    lookup_field = 'slug'

    def get_queryset(self):
        return BlogPost.objects.filter(
            published=True,
            published_at__lte=timezone.now(),
        )


def health_check(request):
    return JsonResponse({'status': 'ok'})
