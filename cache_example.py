import redis
import rd as creds

class CACHE:
    def __init__(self):
        self.connection = redis.Redis(
            host = creds.rdHost,
            port = creds.rdPort,
            db = creds.rdDB,
            password = creds.rdPassWord
        )
    
    def save(self, user):
        try:
            self.connection.hset(('users-{}').format(user['name']),'name',user['name'])
            self.connection.hset(('users-{}').format(user['name']),'email',user['email'])
            self.connection.hset(('users-{}').format(user['name']),'age',user['age'])
            self.connection.expire(('users-{}').format(user['name']), 120)
            return user
        except:
            return { 'info' : 'Não é possível ler os dados' }

    def get(self, name):
        try:
            return {
                "name" : self.connection.hget(('users-{}').format(name), 'name').decode('UTF-8'),
                "email" : self.connection.hget(('users-{}').format(name), 'email').decode('UTF-8'),
                "age" : self.connection.hget(('users-{}').format(name), 'age').decode('UTF-8')
            }
        except:
            return { 'info' : 'Não é possível ler os dados' }