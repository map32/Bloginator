import os, sqlite3, csv, random

db_name = "postsData.db"

def start():

     if (not os.path.exists(db_name)):

        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        q = """create table posts (content text, title text, user_id integer, post_id integer);"""
        c.execute(q)

        q = """insert into posts values ("Hello world", "first", 700, 100);"""
        c.execute(q)

        conn.commit()

def addPost(post, title, user):

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    idd = makeID()

    q = """insert into posts values ("%s", "%s", "%i", "%i")""" %(post, title, findhuman(user), idd) 

    c.execute(q)

    conn.commit()

def findhuman(name):

    conn = sqlite3.connect("membersData.db")
    c = conn.cursor()

    q = (""" select id from members where user = "%s" """)
    q = q%(name)

    for a in c.execute(q):
         return a[0]
    
def makeID():

     conn = sqlite3.connect(db_name)
     c = conn.cursor()

     q = """select post_id from posts"""
     num = random.randint(100,999)

     for x in c.execute(q):
          if x == num:
               makeID()
          else:
               return num

def removePost(pi):
     
     conn = sqlite3.connect(db_name)
     c = conn.cursor()

     q = """delete from posts where post_id = %i"""
     q = q%(pi)

     c.execute(q)

     conn.commit()

def showPosts():

     allPosts = []
     
     conn = sqlite3.connect(db_name)
     c = conn.cursor()

     q = """select * from posts"""

     for a in c.execute(q):
          b = []
          b.append(find(a[2]))
          for x in a:
               b.append(x)
          allPosts.append(b)
          print b

     return allPosts

def find(user):
    conn = sqlite3.connect("membersData.db")
    c = conn.cursor()

    q = """select * from members"""

    for a in c.execute(q):
         print a[2]
         print user
         if user == a[2]:
              return a[0]

#    q = (""" select user from members where user = "%i" """)

#    q = q%(user)

#    for a in c.execute(q):
#         return a[0]


start()
#showPosts()
