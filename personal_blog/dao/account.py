from personal_blog.models.account import Account
from personal_blog.models.base import db


def create_user(name, email, password, is_admin=False):
    account = Account.query.filter_by(email=email).first()
    if account:
        account.name = name
        account.email = email
        account.is_admin = is_admin
    else:
        account = Account(name=name, email=email, is_admin=is_admin)
    account.set_password_hash(password)

    db.session.add(account)
    db.session.commit()
