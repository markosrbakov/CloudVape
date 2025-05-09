from django.contrib import admin
from django.urls import path, include
from CloudVapes import views
from CloudVapes.views import  contact_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('submit-order/', views.submit_order, name='submit_order'),
    path('contact/', contact_view, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
