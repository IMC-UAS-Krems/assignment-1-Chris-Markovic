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
        pass

    def total_listening_seconds(self):
        pass

    def total_listened_minutes(self):
        pass

    def unique_tracks_listened(self):
        pass


class FamilyAccountUser(User):
    def __init__(self, sub_users):
        self.sub_users = []

    def add_sub_user(self, sub_user):
        pass

    def all_members(self):
        pass


class FreeUser(User):
    def __init__(self, MAX_SKIPS_PER_HOUR = 6):
        pass


class PremiumUser(User):
    def __init__(self, subscription_start):
        self.subscription_start = subscription_start


class FamilyMember(User):
    def __init__(self, parent):
        self.parent = parent