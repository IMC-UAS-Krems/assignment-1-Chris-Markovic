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
        self.tracks.append(track)

    def remove_track(self,track_id):
        self.tracks.remove(track_id)

    def total_duration_seconds(self):
        total_duration_seconds = 0
        for track in self.tracks:
            total_duration_seconds += track.duration_seconds
        return total_duration_seconds


class CollaborativePlaylist(Playlist):
    def __init__(self, playlist_id, name, owner, contributors=[]):
        Playlist.__init__(self, playlist_id, name, owner, tracks=[])
        self.contributors = contributors

    def add_contributor(self, user):
        self.contributors.append(user)

    def remove_contributor(self, user):
        self.contributors.remove(user)