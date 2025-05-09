from django.contrib import admin
from django.urls import path, include
from CloudVapes import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('submit-order/', views.submit_order, name='submit_order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)