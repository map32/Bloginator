import csv, pymongo, random
from pymongo import MongoClient

client = MongoClient()
db_name = "data"
userCollection = "users"
postCollection = "posts"

db = client[db_name]
users = db.userCollection
posts = db.postCollection

def addMember(user, password):
    if users.find_one({"username": user}) == None:
        users.insert_one({"username": user, "password": password})

def check():
    for r in users.find():
        print r

def filterUname(user):
    return users.find_one({"username": user}) == None

def checkPass(user, password):
    return users.find_one({"username": user}) != None and users.find_one({"username": user})["password"] == password





# POSTS/COMMENTS

def showPosts():
    return posts.find({}, {"_id": False})

def addPost(post, title, user):
    posts.insert_one({'post': post, 'title': title, 'user': user, 'id': makeID(), 'comments': []})

def findPost(idd):
    a = posts.find_one({'id': idd})
    a['_id'] = str(a['_id'])
    return a
    
def removePost(pi):
    posts.delete_one({'id': pi})

def makeID():
    num = random.randint(100,999)
    for x in posts.find():
        if x['id'] == num:
            makeID()
        else:
            return num
    return num

def addComment(user, post, info):
    posts.update_one({'id': post}, {'$push': {'comments': {'user': user, 'info': info}}}, upsert = True)
        

#addPost("hi im a person","post 1","my_name")
