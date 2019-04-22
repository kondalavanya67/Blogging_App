from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from blog import views
from .views import home

from registration import views as views2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^api/create_blog/',views.createView.as_view()),
    #url(r'^api/register/',views2),
    url(r'^api/Blog/(?P<interest_name>[a-z A-z]+)$', views.BlogView2.as_view()),
    url(r'^api/Blog_id/(?P<blog_id>[0-9]+)$', views.BlogbyIdView2.as_view()),
    path('users/', include('registration.urls')),
    path('home/',include('blog.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
