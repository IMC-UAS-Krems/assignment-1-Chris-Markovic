"""
albums.py
---------
Implement the Album class for collections of AlbumTrack objects.

Classes to implement:
  - Album
"""

class Album:
    def __init__(self, album_id, title, artist, release_year, tracks):
        self.album_id = album_id
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)

    def track_ids(self):
        ids = []
        for track in self.tracks:
            ids.append(track.track_id)
        return ids
    def duration_seconds(self):
        total_duration = 0
        for track in self.tracks:
            total_duration += track.duration_seconds
        return total_duration

