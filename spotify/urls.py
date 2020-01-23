from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
app_name='spotify'
urlpatterns = [
    path('short_term_artists', views.ShortTermArtistsView.as_view(), name='short_term_artists'),
    path('medium_term_artists', views.MediumTermArtistsView.as_view(), name='medium_term_artists'),
    path('long_term_artists', views.LongTermArtistsView.as_view(), name='long_term_artists'),
    path('short_term_tracks', views.ShortTermTracksView.as_view(), name='short_term_tracks'),
    path('medium_term_tracks', views.MediumTermTracksView.as_view(), name='medium_term_tracks'),
    path('long_term_tracks', views.LongTermTracksView.as_view(), name='long_term_tracks'),
    path('', views.MainView.as_view(), name='all'),


]



