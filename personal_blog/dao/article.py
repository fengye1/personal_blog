

from personal_blog.models.article import Article
from personal_blog.models.base import db


def updateArticle(title,content,category_id,id=None):
    if id:
        article = Article.query.get(id)
    else:
        article = Article()
    if article.title != title:
        article_title = Article.query.filter_by(title=title).first()
        if article_title:
            return False
        article.title = title
    article.content = content
    article.category_id = category_id
    db.session.add(article)
    db.session.commit()
    return article


def deleteArticle(id):
    """文章删除"""
    Article.query.get(id).delete()
    db.session.commit()

