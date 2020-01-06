import time
import redis
import rd as creds

connection = redis.Redis(host = creds.rdHost, port = creds.rdPort, db = creds.rdDB)

print("\n Trabalhando com variáveis comuns e Strings\n")
print(connection.set('Greeting', 'Hello World!'))
print(connection.get('Greeting'))

print("\n Contadores com incremento e decremento \n")
print(connection.set('counter', '100'))
print(connection.get('counter'))
print(connection.incr('counter'))
print(connection.get('counter'))
print(connection.decr('counter'))
print(connection.get('counter'))

print("\n Dados com tempo de vida \n")
print(connection.set('user', 'Vou sumir em 5 segundos'))
print(connection.expire('user',5))
print(connection.get('user'))
time.sleep(5)
print(connection.get('user'))

print("\n Vetores e demais estruturas de listas \n")
connection.delete('list')
for i in range(10):
    print(connection.rpush('list', (i + 1) ))
print(connection.lrange('list',0,-1))
for i in range(10):
    print(connection.rpop('list'))

vetor = [1,2,3,4,5]
print(connection.rpush('list', *vetor))
print(connection.lrange('list',0,-1))


print("\n")