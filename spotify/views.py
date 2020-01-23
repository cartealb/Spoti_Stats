from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from spotify.spotify import createHTMLFile
from rest_framework.authtoken.views import ObtainAuthToken
import spotipy
import logging
import json
from social_django.models import UserSocialAuth
import spotipy.util as util
from django.contrib.auth import logout


class MainView(LoginRequiredMixin, View) :
    def get(self, request):
        user = request.user
        auth_json = request.user.social_auth.values_list('extra_data')
        auth_json = auth_json[0][0]
        token = auth_json['access_token']

        username = request.user.social_auth.values_list('uid')[0][0]

        spotify_obj = spotipy.Spotify(auth=token)
        print(spotify_obj._auth)
        print(token)

        createHTMLFile('Artists', 'short_term', spotify_obj)

        #return render(request, createHTMLFile('Artists', 'short_term', spotify_obj))
        return render(request, 'spotify/spotify_user_list.html')


class ShortTermArtistsView(LoginRequiredMixin, View) :
    def get(self, request):
        user = request.user
        auth_json = request.user.social_auth.values_list('extra_data')
        auth_json = auth_json[0][0]
        token = auth_json['access_token']

        username = request.user.social_auth.values_list('uid')[0][0]
        try:
            spotify_obj = spotipy.Spotify(auth=token)
            createHTMLFile('Artists', 'short_term', spotify_obj)
        except:
            logout(request)



        return render(request, 'spotify/spotify_user_list.html')

class MediumTermArtistsView(LoginRequiredMixin, View) :
    def get(self, request):
        user = request.user
        auth_json = request.user.social_auth.values_list('extra_data')
        auth_json = auth_json[0][0]
        token = auth_json['access_token']

        username = request.user.social_auth.values_list('uid')[0][0]
        try:
            spotify_obj = spotipy.Spotify(auth=token)
            createHTMLFile('Artists', 'medium_term', spotify_obj)
        except:
           logout(request)

        return render(request, 'spotify/spotify_user_list.html')


class LongTermArtistsView(LoginRequiredMixin, View) :
    def get(self, request):
        user = request.user
        auth_json = request.user.social_auth.values_list('extra_data')
        auth_json = auth_json[0][0]
        token = auth_json['access_token']

        username = request.user.social_auth.values_list('uid')[0][0]
        try:
            spotify_obj = spotipy.Spotify(auth=token)
            createHTMLFile('Artists', 'long_term', spotify_obj)
        except:
            logout(request)


        return render(request, 'spotify/spotify_user_list.html')

class ShortTermTracksView(LoginRequiredMixin, View) :
    def get(self, request):
        user = request.user
        auth_json = request.user.social_auth.values_list('extra_data')
        auth_json = auth_json[0][0]
        token = auth_json['access_token']

        username = request.user.social_auth.values_list('uid')[0][0]
        try:
            spotify_obj = spotipy.Spotify(auth=token)
            createHTMLFile('Tracks', 'short_term', spotify_obj)
        except:
            logout(request)
            # from social_django.utils import load_strategy
            # social = user.social_auth.get(provider='spotify')
            # strategy = load_strategy()
            # auth_json = request.user.social_auth.values_list('extra_data')
            # auth_json = auth_json[0][0]
            # token = auth_json['access_token']
            # spotify_obj = spotipy.Spotify(auth=token)

        return render(request, 'spotify/spotify_user_list.html')

class MediumTermTracksView(LoginRequiredMixin, View) :
    def get(self, request):
        user = request.user
        auth_json = request.user.social_auth.values_list('extra_data')
        auth_json = auth_json[0][0]
        token = auth_json['access_token']

        username = request.user.social_auth.values_list('uid')[0][0]
        try:
            spotify_obj = spotipy.Spotify(auth=token)
            createHTMLFile('Tracks', 'medium_term', spotify_obj)
        except:
            logout(request)

        return render(request, 'spotify/spotify_user_list.html')

class LongTermTracksView(LoginRequiredMixin, View) :
    def get(self, request):
        user = request.user
        auth_json = request.user.social_auth.values_list('extra_data')
        auth_json = auth_json[0][0]
        token = auth_json['access_token']

        username = request.user.social_auth.values_list('uid')[0][0]
        try:
            spotify_obj = spotipy.Spotify(auth=token)
            createHTMLFile('Tracks', 'long_term', spotify_obj)
        except:
            logout(request)


        return render(request, 'spotify/spotify_user_list.html')




