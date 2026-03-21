"""
platform.py
-----------
Implement the central StreamingPlatform class that orchestrates all domain entities
and provides query methods for analytics.

Classes to implement:
  - StreamingPlatform
"""

class StreamingPlatform:
    def __init__(self, name,_catalogue, _users, _artists, _albums, _playlists, _session):
        self.name = name
        self._catalogue = _catalogue
        self._users = _users
        self._artists = _artists
        self._albums = _albums
        self._playlists = _playlists
        self._session = _session

    def add_track(self, track):
        pass

    def add_user(self, user):
        pass

    def add_artist(self, artist):
        pass

    def add_album(self, album):
        pass

    def add_playlist(self, playlist):
        pass

    def record_session(self, session):
        pass

    def get_track(self, track_id):
        pass

    def get_user(self, user_id):
        pass

    def get_artist(self, artist_id):
        pass

    def get_album(self, album_id):
        pass

    def all_users(self):
        pass

    def all_tracks(self):
        pass