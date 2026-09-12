from django.urls import path
from .views import BlogDetailView, BlogListView, LeadCreateView, SiteDataView, health_check

urlpatterns = [
    path('health/', health_check, name='health'),
    path('site/', SiteDataView.as_view(), name='site-data'),
    path('leads/', LeadCreateView.as_view(), name='lead-create'),
    path('blog/', BlogListView.as_view(), name='blog-list'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
]
