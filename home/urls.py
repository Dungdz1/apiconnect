from django.urls import path,re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('sinhvien/', views.sinhvien_list),
    path('sinhviendetail/<str:pk>/', views.sinhviendetail),
    path('lop/', views.lop_list),
    path('lopdetail/<str:pk>/', views.lopdetail),
    path('api/schema/',SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')

]