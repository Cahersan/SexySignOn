from datetime import datetime
from redis import Redis

from redis_sessions.session import SessionStore

from users.models import User


def get_logged_users():
    # Query all non-expired sessions
    redconn = Redis()
    store = SessionStore()
    
    sessions = [redconn.get(key) for key in redconn.keys()]

    uid_list = []

    # Build a list of user ids from that query
    for session_data in sessions:
        data = store.decode(session_data)
        uid_list.append(data.get('_auth_user_id', None))

    # Query all logged in users based on id list
    return User.objects.filter(id__in=uid_list)

