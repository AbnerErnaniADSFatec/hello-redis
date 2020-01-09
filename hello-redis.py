import time
import redis
import rd as creds

connection = redis.Redis(host = creds.rdHost, port = creds.rdPort, db = creds.rdDB, password = creds.rdPassWord)

print("\n Saída de dados com objetos em BYTES \n")

print("\n Trabalhando com variáveis comuns e Strings\n")
print(connection.set('Greeting', 'Hello World!'))
print(connection.get('Greeting').decode('UTF-8'))

print("\n Contadores com incremento e decremento \n")
print(connection.set('counter', '100'))
print(connection.get('counter').decode('UTF-8'))
print(connection.incr('counter'))
print(connection.get('counter').decode('UTF-8'))
print(connection.decr('counter'))
print(connection.get('counter').decode('UTF-8'))

print("\n Dados com tempo de vida \n")
print(connection.set('user', 'Vou sumir em 5 segundos'))
print(connection.expire('user',5))
print(connection.get('user').decode('UTF-8'))
time.sleep(5)
print(connection.get('user'))

print("\n Vetores e demais estruturas de listas \n")
connection.delete('list')
for i in range(10):
    print(connection.rpush('list', (i + 1)))
print(connection.lrange('list',0,-1))
for i in range(10):
    print(connection.rpop('list').decode('UTF-8'))

vetor = [1,2,3,4,5]
print(connection.rpush('list', *vetor))
print(connection.lrange('list',0,-1))

print("\n Demais estruturas de dados como Dicionários \n")
print(connection.set('person:id', '01'))
print(connection.set('person:name', 'abner'))
print(connection.set('person:company', 'INPE'))
print(connection.set('person:position', 'web developer'))
print(connection.get('person:name').decode('UTF-8'))

print("\n Lista de Objetos no Redis \n")
print(connection.hset('users-01','id','01'))
print(connection.hset('users-01','name', 'abner'))
print(connection.hset('users-01', 'company', 'INPE'))
print(connection.hset('users-01', 'position', 'web developer'))
print(connection.hgetall('users-01')[('name').encode('UTF-8')].decode('UTF-8'))

print("\n")