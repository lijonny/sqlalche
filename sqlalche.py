#coding:utf8
from flask import Flask,render_template,views,request
from sqlalchemy_demo import Articles,session,Author
from sqlalchemy.orm import sessionmaker
app = Flask(__name__)


@app.route('/',methods=['get'])
def index():
    print session
    articles = session.query(Articles).all()
    context={
        'articles':articles
    }
    return render_template('index.html',**context)
class Pull_articles(views.MethodView):
    def get(self):
        return render_template('pull.html')
    def post(self):
        title = request.form.get('title')
        detail = request.form.get('content')
        author = request.form.get('author')



        auth = session.query(Author).filter(Author.name==author).first()
        if not auth:
            authors = Author(name=author)
        article = Articles(title=title, detail=detail)
        article.author = auth
        session.add(article)
        session.commit()

        return 'add article successed'
app.add_url_rule('/pull/',view_func=Pull_articles.as_view('pull'))
@app.route('/detail/<int:id>')
def detail(id):
    article = session.query(Articles).filter_by(id=id).first()
    if article:
        return render_template('detail.html',article=article)
    else:
        return u'没有你要找的文章'
#作者页面，展示作者的所有文章
@app.route('/author/<int:user_id>')
def author(user_id):
    author = session.query(Author).filter_by(id=user_id).first()
    if author:
        articles = author.articles
        return render_template('author.html',articles=articles,author=author)
    else:
        return u'没有你要找的author'
print app.url_map
if __name__ == '__main__':
    app.run(debug=True)
