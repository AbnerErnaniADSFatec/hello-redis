import json
import csv
import pandas as pd
from cache_example import CACHE
from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource
from flask_jsonpify import *

app = Flask(__name__)
CORS(app)

def getUsers():
    try:
        users = pd.read_csv('db/users.csv', sep = ',')
        return users
    except:
        return {}

def getUser(name):
    try:
        users = getUsers()
        user = {}
        for i in range(len(users)):
            if users['name'][i] == name:
                user = { 
                    'name' : users['name'][i],
                    'email' : users['email'][i],
                    'age' : int(users['age'][i])
                }
                break
        return user
    except:
        return {}

def removeUser(name):
    try:
        users = getUsers()
        userToRemove = getUser(name)
        with open('db/users.csv', mode = 'w', encoding = 'utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['name','email','age'])
            writer.writeheader()
            for i in range(len(users)):
                if users['name'][i] != userToRemove['name']:
                    writer.writerow({
                        'name' : users['name'][i],
                        'email' : users['email'][i],
                        'age' : int(users['age'][i])
                    })
        return userToRemove
    except:
        return {}

def addUser(name,email,age):
    try:
        users = getUsers()
        if not getUser(name):
            with open('db/users.csv', mode = 'w', encoding = 'utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['name','email','age'])
                writer.writeheader()
                for i in range(len(users)):
                    writer.writerow({
                        'name' : users['name'][i],
                        'email' : users['email'][i],
                        'age' : int(users['age'][i])
                    })
                writer.writerow({
                    'name' : name,
                    'email' : email,
                    'age' : int(age)
                })
        return {
            'name' : name,
            'email' : email,
            'age' : int(age)
        }
    except:
        return {}

def updateUser(name,email,age):
    try:
        remove = removeUser(name)
        add = addUser(name,email,age)
        return add
    except:
        return {}

@app.route("/db/users/add", methods=['GET','POST'])
def add():
    if request.method == 'POST':
        try:
            add = addUser(
                request.get_json(force=True)['name'],
                request.get_json(force=True)['email'],
                request.get_json(force=True)['age']
            )
            return jsonify(add)
        except:
            return jsonify({ 'info' : 'Impossivel ler os dados' })
    if request.method == 'GET':
        return jsonify({ 'info' : 'metodo GET não permitido para este URL' })

@app.route("/db/users/update", methods=['GET','POST'])
def update():
    if request.method == 'POST':
        try:
            update = updateUser(
                request.get_json(force=True)['name'],
                request.get_json(force=True)['email'],
                request.get_json(force=True)['age']
            )
            return jsonify(update)
        except:
            return jsonify({ 'info' : 'Impossivel ler os dados' })
    if request.method == 'GET':
        return jsonify({ 'info' : 'metodo GET não permitido para este URL' })

@app.route("/db/users/remove", methods=['GET','POST'])
def remove():
    if request.method == 'POST':
        try:
            remove = removeUser(request.get_json(force=True)['name'])
            return jsonify(remove)
        except:
            return jsonify({ 'info' : 'Impossivel ler os dados' })
    if request.method == 'GET':
        return jsonify({ 'info' : 'metodo GET não permitido para este URL' })

@app.route("/db/users", methods=['GET','POST'])
def users():
    if request.method == 'POST':
        return jsonify({ 'info' : 'metodo GET não permitido para este URL' })
    if request.method == 'GET':
        try:
            users = getUsers()
            return jsonify(users.to_dict())
        except:
            return jsonify({ 'info' : 'Impossível ler os dados' })

@app.route("/db/user/<name>", methods=['GET','POST'])
def user(name):
    if request.method == 'POST':
        return jsonify({ 'info' : 'metodo POST não permitido para este URL' })
    if request.method == 'GET':
        try:
            user = getUser(str(name))
            return jsonify(user)
        except:
            return jsonify({ 'info' : 'Impossivel ler os dados' })

@app.route("/db/user/<name>/login", methods=['GET','POST'])
def login(name):
    if request.method == 'POST':
        return jsonify({ 'info' : 'metodo POST não permitido para este URL' })
    if request.method == 'GET':
        try:
            cache = CACHE()
            user = cache.save(getUser(str(name)))
            return jsonify(user)
        except:
            return jsonify({ 'info' : 'Impossivel ler os dados' })

@app.route("/db/user/<name>/status", methods=['GET','POST'])
def status(name):
    if request.method == 'POST':
        return jsonify({ 'info' : 'metodo POST não permitido para este URL' })
    if request.method == 'GET':
        try:
            cache = CACHE()
            user = cache.get(str(name))
            try:
                print(user['name'])
                user['status'] = 'A sessão está aberta!'
                user['logged'] = True
                return jsonify(user)
            except:
                print(user['info'])
                user['status'] = 'A sessão do usuário expirou!'
                user['logged'] = False
                return jsonify(user)
        except:
            return jsonify({ 'info' : 'Impossivel ler os dados' })

if __name__ == '__main__':
    app.run( host = '0.0.0.0' )