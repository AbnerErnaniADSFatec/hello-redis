# Hello World [REDIS](https://redis.io)

Funcionamento da biblioteca [`redis`](https://pypi.org/project/redis/) para o controle do servidor de estrutura de dados em Python e controle de cacheamento de sessões. REDIS significa REmote DIctionary Server ou servidor de dicionário remoto.

### Instalação do servidor redis
#### => [Docker](https://hub.docker.com/_/redis/)
#### => Local
```
# apt update && apt install redis-server
```
```
# systemctl status redis.service
```

### Instalação rápida da biblioteca para a execução de `hello-redis.py`

```
$ sudo pip install redis
```

### Instalação das bibliotecas necessários para o sistema de cache em `server.py`

```
$ sudo pip install -r requirements.txt
```