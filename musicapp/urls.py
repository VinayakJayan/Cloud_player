from django.urls import path
from . import views

urlpatterns = [
    # Song URLs
    path('songs/', views.song_list, name='song_list'),
    path('songs/<int:pk>/', views.song_detail, name='song_detail'),

    # Album URLs
    path('albums/', views.album_list, name='album_list'),
    path('albums/<int:pk>/', views.album_detail, name='album_detail'),

    # Playlist URLs
    path('playlists/', views.playlist_list, name='playlist_list'),
    path('playlists/<int:pk>/', views.playlist_detail, name='playlist_detail'),

    # Search URL
    path('search/', views.search, name='search'),

    # User URLs
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]

