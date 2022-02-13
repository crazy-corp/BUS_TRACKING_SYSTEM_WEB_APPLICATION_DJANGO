from django.contrib import admin
from SFE import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings
urlpatterns = [
    path("",views.sfe),
	path('', include('SFE.urls')),
    path('admin/', admin.site.urls,name='admin'),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))
    ),
]