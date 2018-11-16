#Personal_blog


启动 Python:
> FLASK_APP=personal_blog FLASK_ENV=development flask run

效果预览:
用浏览器打开： http://localhost:5000[http://localhost:5000]


启动 Python Shell:
> cd $WorkSpaceRoot
> FLASK_APP=personal_blog FLASK_ENV=development flask shell

数据库迁移：

迁移：
> FLASK_APP=personal_blog FLASK_ENV=development flask db migrate

提交更新：
>>> FLASK_APP=personal_blog FLASK_ENV=development flask db upgrade

回退：

> FLASK_APP=personal_blog FLASK_ENV=development flask db downgrade
