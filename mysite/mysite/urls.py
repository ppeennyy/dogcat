from django.conf.urls import patterns, include, url
from django.contrib import admin
#from mysite.views import here
from django.conf import settings
from django.conf.urls.static import static
from mysite.views import index
 
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    #url(r'^here/$', here)
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
