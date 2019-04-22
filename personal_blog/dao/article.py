from personal_blog.models.article import Article
from personal_blog.models.base import db


def update_article(title, content, category_id, id=None):
    if id:
        article = Article.query.get(id)
    else:
        article = Article()
    print("ddddddddddddddddd12")
    if article.title != title:
        print("=============>>>aa")
        article_title = Article.query.filter(Article.title==title).first()
        print("=============>>>", article_title)
        if article_title:
            return False
        article.title = title
    print("ddddddddddddddddd2")
    article.content = content
    if category_id:
        article.category_id = category_id
    print("ddddddddddddddddd")
    db.session.add(article)
    db.session.commit()
    return article


def delete_article(id):
    """文章删除"""
    Article.query.get(id).delete()
    db.session.commit()
