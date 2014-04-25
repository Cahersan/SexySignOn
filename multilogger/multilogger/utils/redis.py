import redis
from users.models import User

class RedisUtility(redis.Redis):

    def __init__(self, *args, **kwargs):
        super(RedisUtility, self).__init__(*args, **kwargs)

    def copy_users(self):
        users = User.objects.all()
        l = [user.username for user in users] 
        self.set("Users", l)
