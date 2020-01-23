from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Keep
    path('spotify/', include('spotify.urls')),                   # Add
    url(r'^auth/', include('social_django.urls', namespace='social')),
]