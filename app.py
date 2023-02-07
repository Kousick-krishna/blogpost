from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db = SQLAlchemy(app)
all_posts=[
    {
        'title' : 'post1',
        'content':'hello how are you',
        'author': 'kousick'
    },
    {
        'title': 'post2',
        'content' : 'hey how are you'
    }
]


class Blogpost(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content  = db.Column(db.Text,nullable=False)
    author  =db.Column(db.String(20),nullable=False,default="N/A")
   
    
    def __repr__(self):
        return 'Blogpost'+str(self.id)

@app.route('/')
def hello():
    return "Hello,kousick"

@app.route('/posts', methods=['POST','GET'])
def posts():
    if request.method=='POST':
        post_title=request.form['title']
        post_content=request.form['content']
        post_author=request.form['author']
        new_post=Blogpost(title=post_title,content=post_content,author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')

     
    else:
        all_posts=Blogpost.query.all()
        return render_template('posts.html',posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
        
        
       

       


   






