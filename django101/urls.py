from django.conf.urls import url, include
from django.contrib import admin
import social

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',       include('social.urls', namespace='social')),
]   