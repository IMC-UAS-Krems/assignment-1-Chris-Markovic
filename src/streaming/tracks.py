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

    def duration_minutes(self):
        pass

class Song(Track):
    def __init__(self, artist):
        self.artist = artist

class AlbumTrack(Song):
    def __init__(self, track_number, album):
        self.track_number = track_number
        self.album = album

class SingleRelease(Song):
    def __init__(self, release_date):
        self.release_date = release_date

class Podcast(Track):
    def __init__(self, host, description):
        self.host = host
        self.description = description

class NarrativeEpisode(Podcast):
    def __init__(self,season, episode_number):
        self.season = season
        self.episode_number = episode_number

class InterviewEpisode(Podcast):
    def __init__(self, guest):
        self.guest = guest

class AudiobookTrack(Track):
    def __init__(self, author, narrator):
        self.author = author
        self.narrator = narrator


