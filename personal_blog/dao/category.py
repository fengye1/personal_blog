from personal_blog.models.category import Category
from personal_blog.models.base import db


def category_create(label, description, is_show=True, position=None):
    """分类创建"""
    if not position:
        position = db.session.query(Category.position).obder_by(Category.position.desc()).first() or 1
    category = Category(label=label, description=description, is_show=is_show, position=position)
    db.session.add(category)
    db.session.commit()
    return category


def category_edit(id, label, description, is_show=True):
    """分类编辑"""
    category = Category.query.get(id)
    if category:
        category.label = label
        category.desc = description,
        category.is_show = is_show
        db.session.add(category)
        db.session.commit()
        return category
    else:
        return None


def category_delete(id):
    """删除分类"""
    category = Category.query.get(id)
    if category:
        db.session.delete(category)
        db.session.commit()
