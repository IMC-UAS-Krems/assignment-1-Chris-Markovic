"""
tracks.py
---------
Implement the class hierarchy for all playable content on the platform.

Classes to implement:
  - Track (abstract base class)
    - Song
      - SingleRelease
      - AlbumTrack
    - Podcast
      - InterviewEpisode
      - NarrativeEpisode
    - AudiobookTrack
"""


class Track:
    def __init__(self, track_id, title, duration_seconds, genre):
        self.track_id = track_id
        self.title = title
        self.duration_seconds = duration_seconds
        self.genre = genre
    def __eq__(self, other):
        if not isinstance(other, Track):
            return False
        return self.track_id == other.track_id

    def duration_minutes(self):
        return float(self.duration_seconds / 60)

class Song(Track):
    def __init__(self,track_id, title, duration_seconds, genre, artist):
        Track.__init__(self, track_id, title, duration_seconds, genre)
        self.artist = artist

class AlbumTrack(Song):
    def __init__(self, track_id, title, duration_seconds, genre, artist, track_number, album=None):
        Song.__init__(self, track_id, title, duration_seconds, genre, artist)
        self.track_number = track_number
        self.album = album

class SingleRelease(Song):
    def __init__(self, track_id, title, duration_seconds, genre, artist, release_date):
        Song.__init__(self, track_id, title, duration_seconds, genre, artist)
        self.release_date = release_date

class Podcast(Track):
    def __init__(self, track_id, title, duration_seconds, genre, host, description=""):
        Track.__init__(self, track_id, title, duration_seconds, genre)
        self.host = host
        self.description = description

class NarrativeEpisode(Podcast):
    def __init__(self, track_id, title, duration_seconds, genre, host, season, episode_number, description=""):
        Podcast.__init__(self, track_id, title, duration_seconds, genre, host, description)
        self.season = season
        self.episode_number = episode_number

class InterviewEpisode(Podcast):
    def __init__(self,track_id, title, duration_seconds, genre, host, guest, description=""):
        Podcast.__init__(self, track_id, title, duration_seconds, genre, host, description)
        self.guest = guest

class AudiobookTrack(Track):
    def __init__(self,track_id, title, duration_seconds, genre, author, narrator):
        Track.__init__(self, track_id, title, duration_seconds, genre)
        self.author = author
        self.narrator = narrator


