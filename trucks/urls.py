from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'trucks.views.home', name='home'),
    url(r'^about/$', 'trucks.views.about', name='about'),
)
