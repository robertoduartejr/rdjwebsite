"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf.urls.static import static
from django.conf import settings
from siteblog import views
from django.views.static import serve

handler404 = 'siteblog.views.custom_page_not_found_view'
handler500 = 'siteblog.views.custom_error_view'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('',views.home,name='home'),
    path('provide_json/<int:num_projects>/<slug:slug>',views.provide_json,name='provide_json'),
    path('provide_json_posts/<int:num_posts>/<slug:slug>',views.provide_json_posts, name='provide_json_posts'),
    path('provide_json_users/',views.provide_json_users,name='provide_json_users'),
    path('project/<slug:slug>',views.project),
    path('tag/<slug:slug>/',views.tagged,name="tagged"),
    path('downloadfile/',views.downloadfile,name="downloadfile"),
    path('accounts/', include('allauth.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    #path('post/', views.post, name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




