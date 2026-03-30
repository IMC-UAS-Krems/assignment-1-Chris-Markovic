"""
users.py
--------
Implement the class hierarchy for platform users.

Classes to implement:
  - User (base class)
    - FreeUser
    - PremiumUser
    - FamilyAccountUser
    - FamilyMember
"""


class User:
    def __init__(self, user_id, name, age, sessions):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

    def total_listening_seconds(self):
        global listening_seconds
        listening_seconds = 0
        for session in self.sessions:
            listening_seconds += session.duration_listened_seconds
        return listening_seconds

    def total_listened_minutes(self):
        global listening_seconds
        return listening_seconds / 60

    def unique_tracks_listened(self):
        unique_tracks = []
        for session in self.sessions:
            if session.track.track_id not in unique_tracks:
                unique_tracks.append(session.track.track_id)
        return len(unique_tracks)

class FamilyAccountUser(User):
    def __init__(self, user_id, name, age, sessions, sub_users):
        User.__init__(self, user_id, name, age, sessions)
        self.sub_users = []

    def add_sub_user(self, sub_user):
        self.sub_users.append(sub_user)

    def all_members(self):
        pass


class FreeUser(User):
    def __init__(self, user_id, name, age, sessions, MAX_SKIPS_PER_HOUR = 6):
        User.__init__(self, user_id, name, age, sessions)
        pass


class PremiumUser(User):
    def __init__(self, user_id, name, age, sessions, subscription_start):
        User.__init__(self, user_id, name, age, sessions)
        self.subscription_start = subscription_start


class FamilyMember(User):
    def __init__(self, user_id, name, age, sessions, parent):
        User.__init__(self, user_id, name, age, sessions)
        self.parent = parent