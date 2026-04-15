"""
platform.py
-----------
Implement the central StreamingPlatform class that orchestrates all domain entities
and provides query methods for analytics.

Classes to implement:
  - StreamingPlatform
"""

from datetime import datetime, timedelta #found this on google to track current time and date: https://www.geeksforgeeks.org/python/python-datetime-timedelta-function/

from streaming.tracks import Song
from streaming.users import PremiumUser, FamilyAccountUser, FreeUser, FamilyMember


class StreamingPlatform:
    def __init__(self, name):
        self.name = name
        self._catalogue = {} #dictionary with tracks
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
"""
Return the total cumulative listening time (in minutes) across all users for a given time period.
Sum up the listening duration for all sessions that fall within the specified datetime window 
(inclusive on both ends).
"""



#Q1 DONE!
def total_listening_time_minutes(self,start,end):
    total_listened_min_app = 0
    for session in self._session:
        if start <= session.timestamp <= end:
            total_listened_min_app += session.duration_listened_seconds
    return total_listened_min_app/60

"""
Compute the average number of unique tracks listened to per PremiumUser in the last days days (default 30).
Only count distinct tracks for sessions within the time window. Return 0.0 if there are no premium users.
"""

#Q2 DONE!
def avg_unique_tracks_per_premium_user(self, days=30):
        from users import PremiumUser
        premium_users = []

        for user in self._users.values():
            if isinstance(user, PremiumUser):
                premium_users.append(user)

        start_date = datetime.now() - timedelta(days=days)  #found on google, link on line 11 next to import
        total_unique_tracks = 0
        if premium_users:
            for user in premium_users:
                unique_tracks = []
                for session in user.sessions:
                    if start_date <= session.timestamp and session.track.track_id not in unique_tracks:
                        unique_tracks.append(session.track.track_id)
                total_unique_tracks += len(unique_tracks)

        return total_unique_tracks/len(premium_users)

"""
Return the track with the highest number of distinct listeners (not total plays) in the catalogue.
 Count the number of unique users who have listened to each track and return the one with the most.
 Return None if no sessions exist.
"""

#Q3 DONE!
def track_with_most_distinct_listeners(self):
        if not self._session:
            return None

        track_listeners = {}
        for session in self._session:
            track_id = session.track.track_id
            user_id = session.user.user_id

            if track_id not in track_listeners:
                track_listeners[track_id] = set()
            track_listeners[track_id].add(user_id)

        most_distinct_listeners = max(track_listeners, key= lambda x: track_listeners[x])
        return self._catalogue[most_distinct_listeners]


"""
For each user subtype (e.g., FreeUser, PremiumUser, FamilyAccountUser, FamilyMember), 
compute the average session duration (in seconds) and return them ranked from longest to shortest. 
Return as a list of (type_name, average_duration_seconds) tuples.
"""

#Q4 DONE!
def avg_session_duration_by_user_type(self):
    total_times = {}
    total_counts = {}

    for session in self._session:
        u_type = type(session.user).__name__

        total_times[u_type] = total_times.get(u_type, 0) + session.duration_listened_seconds
        total_counts[u_type] = total_counts.get(u_type, 0) + 1
    averages = []
    for u_type in total_times:
        avg = total_times[u_type] / total_counts[u_type]
        averages.append((u_type, avg))

    averages.sort(key=lambda x: x[1], reverse=True)
    return averages


"""
Return the total listening time (in minutes) attributed to tracks associated 
with FamilyAccountUser sub-accounts where the sub-account holder(i.e., FamilyMember)
 is under the specified age threshold (default 18, exclusive).
 For example, with threshold 18, count only family members with age < 18.
"""

#Q5 DONE!
def total_listening_time_underage_sub_users_minutes(self, age_threshold= 18):
    from users import FamilyMember
    total_minutes = 0
    if self._users:
        for user in self._users.values():
            if isinstance(user, PremiumUser) and user.age < age_threshold:
                total_minutes += user.total_listening_minutes()
    return total_minutes


"""
Identify the top n artists (default 5) ranked by total cumulative listening time across all their tracks. 
Only count listening time for tracks where isinstance(track, Song) is true (exclude podcasts and audiobooks). 
Return as a list of (Artist, total_minutes) tuples, sorted from highest to lowest listening time.
"""

#Q6 DONE!
def top_artists_by_listening_time(self, n=5):
    top_artists = {}
    for session in self._session:
        if isinstance(session.track, Song):
            artist = session.track.artist
            if artist not in top_artists:
                top_artists[artist] = 0
            top_artists[artist] += session.duration_listened_minutes()
    top_n_artists = sorted(top_artists.items(), key=lambda x: x[1], reverse=True)[:n]
    return top_n_artists


"""
Given a user ID, return their most frequently listened-to genre and the percentage of 
their total listening time it accounts for.
 Return a (genre, percentage) tuple where percentage is in the range [0, 100], 
 or None if the user doesn't exist or has no listening history.
"""

#Q7 DONE!
def user_top_genre(self, user_id):

    if user_id not in self._users:
        return None
    user = self._users[user_id]
    if not user.sessions:
        return None
    genre_times = {}
    total_time = 0
    for session in user.sessions:
        genre = session.track.genre
        genre_times[genre] = genre_times.get(genre, 0) + session.duration_listened_seconds
        total_time += session.duration_listened_seconds


    top_genre = max(genre_times, key=genre_times.get)
    percentage = (genre_times[top_genre] / total_time) * 100
    return (top_genre, percentage)

"""
Return all CollaborativePlaylist instances that contain tracks from more than threshold (default 3) distinct artists. 
Only Song tracks count toward the artist count (exclude Podcast and AudiobookTrack which don't have artists). 
Return playlists in the order they were registered.
"""

#Q8 DONE!
def collaborative_playlists_with_many_artists(self, threshold= 3):
    from playlists import CollaborativePlaylist
    from tracks import Song

    diverse_playlists = []
    for playlist in self.playlists.values():
        if isinstance(playlist, CollaborativePlaylist):
            distinct_artists = set()
            for track in playlist.tracks:
                if isinstance(track, Song):
                    distinct_artists.add(track.artist)

            if len(distinct_artists) > threshold:
                diverse_playlists.append(playlist)
    return diverse_playlists


"""
Compute the average number of tracks per playlist, distinguishing between standard Playlist and 
CollaborativePlaylist instances. Return a dictionary with keys "Playlist" and "CollaborativePlaylist" 
mapped to their respective averages. Return 0.0 for a type with no instances.
"""

#Q9 DONE!
def avg_tracks_per_playlist_type(self):
    from playlists import Playlist, CollaborativePlaylist
    stats = {
        "Playlist": {"tracks": 0, "count": 0},
        "CollaborativePlaylist": {"tracks": 0, "count": 0}
    }
    for playlist in self.playlists.values():
        if type(playlist) is Playlist:
            stats["Playlist"]["tracks"] += len(playlist.tracks)
            stats["Playlist"]["count"] += 1
        elif type(playlist) is CollaborativePlaylist:
            stats["CollaborativePlaylist"]["tracks"] += len(playlist.tracks)
            stats["CollaborativePlaylist"]["count"] += 1

    results = {}
    for playlist_type, number in stats.items():
        if number["count"] > 0:
            results[playlist_type] = number["tracks"] / number["count"]
        else:
            results[playlist_type] = 0.0

    return results

"""
Identify users who have listened to every track on at least one complete Album and return the
 corresponding album titles. A user "completes" an album if their session history includes at least 
 one listen to each track on that album. Return as a list of (User, [album_title, ...]) tuples in registration order. 
 Albums with no tracks are ignored.
"""


#Q10 DONE!
def users_who_completed_albums(self):
    results = []
    for user in self._users.values():
        completed_album_titles = []
        listened_tracks = {session.track for session in user.sessions}
        for item in self._catalogue.values():
            if hasattr(item, 'tracks') and isinstance(item.tracks, list):
                album_tracks = item.tracks
                if not album_tracks:
                    continue
                is_complete = True
                for track in album_tracks:
                    if track not in listened_tracks:
                        is_complete = False
                        break
                if is_complete:
                    completed_album_titles.append(item.title)
        if completed_album_titles:
            results.append((user, completed_album_titles))

    return results



spotify = StreamingPlatform("Spotify")

