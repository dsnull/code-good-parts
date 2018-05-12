from django.conf.urls import include, url
from django.contrib import admin
import api

urlpatterns = [
    # Examples:
    # url(r'^$', 'pndemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
