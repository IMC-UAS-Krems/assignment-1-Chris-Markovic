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
    def __init__(self, user_id, name, age, sessions = None):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.sessions = sessions if sessions is not None else []

    def add_session(self, session):
        self.sessions.append(session)

    def total_listening_seconds(self):
        listening_seconds = 0
        for session in self.sessions:
            listening_seconds += session.duration_listened_seconds
        return listening_seconds

    def total_listening_minutes(self):
        return self.total_listening_seconds()/60

    def unique_tracks_listened(self):
        unique_tracks = set()
        for session in self.sessions:
            unique_tracks.add(session.track.track_id)
        return unique_tracks

class FamilyAccountUser(User):
    def __init__(self, user_id, name, age, sessions = None, sub_users = None):
        User.__init__(self, user_id, name, age, sessions)
        self.sub_users = sub_users if sub_users is not None else []

    def add_sub_user(self, sub_user):
        self.sub_users.append(sub_user)

    def all_members(self):
        return [self] + self.sub_users


class FreeUser(User):
    def __init__(self, user_id, name, age, MAX_SKIPS_PER_HOUR = 6, sessions = None):
        User.__init__(self, user_id, name, age, sessions)



class PremiumUser(User):
    def __init__(self, user_id, name, age, subscription_start, sessions = None):
        User.__init__(self, user_id, name, age, sessions)
        self.subscription_start = subscription_start


class FamilyMember(User):
    def __init__(self, user_id, name, age,parent, sessions = None, sub_users = None):
        User.__init__(self, user_id, name, age, sessions)
        self.parent = parent
        self.sub_users = sub_users if sub_users is not None else []