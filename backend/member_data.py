import os, sqlite3, csv, random 
from pymongo import MongoClient

#ok let's get 2 writing the neato functions m8ies
#it's not like I need to get to gold or anything

'''

def go():

    if (not os.path.exists(db_name)):

        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        q = """create table members (user text, pwd text, id integer);"""
        c.execute(q)

        q = """insert into members values ("James", "Bond", 700);"""
        w = """insert into members values ("Roger", "Rabbit", 101);"""

        c.execute(q)
        c.execute(w)

        conn.commit()

def check():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    x = """SELECT * FROM members"""
    res = c.execute(x)
    for r in res:
        print r

def filterUname(uname):
    
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    q = """select user from members"""

    for i in c.execute(q):
        if i[0] == uname:
            return False
        
    return True

def addMember(u, p):

    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    i = iterate()
    q = """insert into members values ("%s","%s",%i);"""
    q = q%(u,p,i)
    c.execute(q)
    conn.commit()
    
def iterate():

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    q = """select id from members;"""
    num = random.randint(100,999)
    for a in c.execute(q):
        if num == a:
            iterate()
    return num    

def checkPass(uname, passwd):

    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    q = """ select pwd from members where user = "%s" """ 
    q = q%(uname)

    for line in c.execute(q):
        print passwd
        print line[0]
        if line[0] == passwd:
            print "true"
            return True
        else:
            print "false"
            return False



go()    
#check()

'''
