"""
platform.py
-----------
Implement the central StreamingPlatform class that orchestrates all domain entities
and provides query methods for analytics.

Classes to implement:
  - StreamingPlatform
"""



#PRIDAT QUERY METHODS Q1 ATD Z README

class StreamingPlatform:
    def __init__(self, name):
        self.name = name
        self._catalogue = {} #Tracks
        self._users = {}
        self._artists = {}
        self._albums = {}
        self._playlists = {}
        self._session = []

    def add_track(self, track):
        self._catalogue[track.track_id] = track
        return self._catalogue


    def add_user(self, user):
        self._users[user.user_id] = user
        return self._users

    def add_artist(self, artist):
        self._artists[artist.artist_id] = artist
        return self._artists

    def add_album(self, album):
        self._albums[album.album_id] = album
        return self._albums

    def add_playlist(self, playlist):
        self._playlists[playlist.playlist_id] = playlist
        return self._playlists

    def record_session(self, session):
        self._session.append(session)
        return self._session

    def get_track(self, track_id):
        return self._catalogue.get(track_id)

    def get_user(self, user_id):
        return self._users.get(user_id)

    def get_artist(self, artist_id):
        return self._artists.get(artist_id)

    def get_album(self, album_id):
        return self._albums.get(album_id)

    def all_users(self):
        return list(self._users.values())

    def all_tracks(self):
        return list(self._catalogue.values())

    #METHODS

    #Q1
    def total_listening_time_minutes(self,start,end):
        for session in self._session:

    #Q2
    def avg_unique_tracks_per_premium_user(self, days=30):
        pass

    #Q3
    def track_with_most_distinct_listeners(self):
        pass

    #Q4
    def avg_session_duration_by_user_type(self):
        pass

    #Q5
    def total_listening_time_underage_sub_users_minutes(self, age_threshold= 18):
        pass

    #Q6
    def top_artists_by_listening_time(self, n=5):
        pass

    #Q7
    def user_top_genre(self, user_id):
        pass

    #Q8
    def collaborative_playlists_with_many_artists(self, threshold= 3):
        pass

    #Q9
    def avg_tracks_per_playlist_type(self):
        pass

    #Q10
    def users_who_completed_albums(self):
        pass

spotify = StreamingPlatform("Spotify")

