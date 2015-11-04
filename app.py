from flask import Flask, render_template, request, session, redirect
from backend import mongodata

app=Flask(__name__)

@app.route('/')
@app.route('/home',methods=["GET","POST"])
def home():
    #Track whether the user has logged in
    if 'logged' not in session:
        session['logged']=False
    if 'post_til' not in session:
        session['post_til']=10
    if 'in_comments' not in session:
        session['in_comments']=False
    if 'comment_index' not in session:
        session['comment_index']=0
    if request.method=="POST":
        mongodata.addPost(request.form['story'],request.form['title'],session['username'])
    print session['post_til']
    post=mongodata.showPosts().sort('$natural', -1);
    return render_template('home.html',s=session,posts=post)

@app.route('/make_comment',methods=["GET","POST"])
def make_the_goddamn_comment():
    if request.method=="POST":
        theUname = session['username']
        thepostnum = int(session['post_id'])
        thecomment = request.form['thecomment']
        mongodata.addComment(theUname,thepostnum,thecomment)
        print mongodata.findPost(thepostnum)
        session['comments']=mongodata.findPost(session['post_id'])
    return redirect("/")

@app.route('/rm_post',methods=["GET","POST"])
def rm_this_post():
    if request.method=="POST":
        print request.form
        the_post_id = request.form['post_id']
        mongodata.removePost(int(the_post_id))
        return redirect("/home")

@app.route('/add_more_posts/')
def add_up():
    session['post_til']+=10
    return redirect("/home")

@app.route('/remove_more_posts')
def go_back():
    session['post_til']-=10
    return redirect("/home")

@app.route('/set_comment_off')
def set_comment_off():
    session['in_comments']=False
    return redirect("/home")

@app.route('/login',methods=["GET","POST"])
def login():
    if 'logged' not in session:
        session['logged']=False
    #If the user is trying to log in, verify password
    if request.method=="POST":
        if (request.form['button']=="New Account"):
            if (mongodata.filterUname(request.form['username'])):
                mongodata.addMember(request.form['username'], request.form['password'])
                session['logged']=True
                session['username']=request.form['username']
                return redirect('/')
            else:
                return render_template('login.html',s=session,error="Username already taken")
        if (request.form['button']=="login"):
            if mongodata.checkPass(request.form['username'], request.form['password']):
                session['logged']=True
                session['username']=request.form['username']
                return redirect('/')
            else:
                return render_template('login.html',s=session,error="Incorrect Username/Password")
    return render_template('login.html',s=session)

#When a user clicks a button to logout, direct them here, log them out and redirect them
@app.route('/logout')
def logout():
    session['logged'] = False
    return redirect('/login')

@app.route("/comments",methods=["GET","POST"])
def comment():
    if (session['logged']!=True):
        return redirect('/login')
    session['in_comments']=True
    session['comments']=mongodata.findPost(int(request.form['post_id']))
    print session['comments']
    session['post_id']=int(request.form['post_id'])
    session['comment_name']=request.form['comment_name']
    session['comment_text']=request.form['comment_text']
    return redirect('/')


if __name__=="__main__":
    app.debug = True
    app.secret_key="Don't tell anyone!"
    app.run('0.0.0.0', port=8000)
