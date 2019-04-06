from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from blog import views
from .views import home

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', home),
                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),
                  path('api/interest', views.interestView.as_view()),
                  path('api/Blog', views.BlogView.as_view()),
                  url(r'^users/', include('registration.urls')),
                  path('home/', include('blog.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
