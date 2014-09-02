from django.conf.urls import patterns, include, url

from django.views.generic.base import TemplateView
from alipay.views import alipay

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alipay_python.views.home', name='home'),
    # url(r'^alipay_python/', include('alipay_python.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url('^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url('^alipay/1$', alipay, name='alipay'),
)
