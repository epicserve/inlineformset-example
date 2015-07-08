from django.conf.urls import patterns, include
from django.contrib import admin
from django.conf import settings

handler500 = 'utils.views.server_error'

urlpatterns = patterns('')

# Debug/Development URLs
if settings.DEBUG is True:  # pragma: no branch
    urlpatterns += patterns(
        '',
        (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    )

# Admin Site
admin.autodiscover()

# Includes
urlpatterns += patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    (r'', include('books.urls')),
)
