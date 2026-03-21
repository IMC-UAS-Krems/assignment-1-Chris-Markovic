"""
playlists.py
------------
Implement playlist classes for organizing tracks.

Classes to implement:
  - Playlist
    - CollaborativePlaylist
"""

class Playlist:
    def __init__(self, playlist_id, name, owner, tracks):
        self.playlist_id = playlist_id
        self.name = name
        self.owner = owner
        self.tracks = []

    def add_track(self,track):
        pass

    def remove_track(self,track_id):
        pass

    def total_duration_seconds(self):
        pass

class CollaborativePlaylist(Playlist):
    def __init__(self, contributors):
        self.contributors = []

    def add_contributor(self, user):
        pass

    def remove_contributor(self, user):
        pass