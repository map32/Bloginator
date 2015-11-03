import csv, pymongo, random
from pymongo import MongoClient
import datetime

conn = MongoClient()
db = conn['data']
users = db['members']

# USERS

def addMember(user, password):
    if users.find_one({"name": user}) == None:
        users.insert_one({"name": user, "password": password, "posts": []})
#????
def check():
    for r in users.find():
        print r

#????
def filterUname(user):
    return users.find_one({"name": user}) == None

#need to test
def checkPass(user, password):
    return users.find_one({"name": user}) != None and users.find_one({"username": user})["password"] == password


# POSTS

def showPosts():
    users.find({},{"posts":true, "_id":false})

def addPost(user, titl, txt, idd):
    users.update_one({'name': user}, {'$push': {'posts': {'title': titl, 'text': txt, 'created':str(datetime.datetime.now()), 'id':idd, 'comments':[{}]}}}, upsert = False)

def findPost(postid):
    return users.find_one({'id': postid})
    
def removePost(user, postid):
    users.update_one({'name': user}, {'$pull': {'posts': {'id': postid}}})

#need
def makeID():
    num = random.randint(100,999)
    for x in posts.find():
        if x['id'] == num:
            makeID()
        else:
            return num
    return num

# COMMENTS
#need
def findComment(user, postid):
    return

def addComment(user, postid, txt):
    users.update_one({'id': postid}, {'$push': {'posts': {'user': user, 'info': info}}}, upsert = False)

#need        
def removeComment(user, postid, commentid):
    return


#addMember("snl", "fml")
#addPost("snl", "lllllllllllllllafsashi", "saffmhfmh", 6)
#removePost("myrseeer", 1)
