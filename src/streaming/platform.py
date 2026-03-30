"""
platform.py
-----------
Implement the central StreamingPlatform class that orchestrates all domain entities
and provides query methods for analytics.

Classes to implement:
  - StreamingPlatform
"""
from _pyrepl.commands import end
from datetime import datetime, timedelta #found this on google to track current time and date



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

    #Q1 DONE!
    def total_listening_time_minutes(self,start,end):
        total_listened_min_app = 0
        for session in self._session:
            if start <= session.timestamp <= end:
                total_listened_min_app += session.duration_listened_seconds
        return total_listened_min_app/60

    #Q2 DONE!
    def avg_unique_tracks_per_premium_user(self, days=30):
        from users import PremiumUser
        premium_users = []

        for user in self._users.values():
            if isinstance(user, PremiumUser):
                premium_users.append(user)

        start_date = datetime.now() - timedelta(days=days)
        total_unique_tracks = 0
        for user in premium_users:
            unique_tracks = []
            for session in user.sessions:
                if start_date <= session.timestamp and session.track.track_id not in unique_tracks:
                    unique_tracks.append(session.track.track_id)
            total_unique_tracks += len(unique_tracks)

        return total_unique_tracks/len(premium_users)



    #Q3..
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

