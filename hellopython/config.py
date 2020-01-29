import os
import sys

from hellopython import app


'''
数据库文件一般放到项目根目录即可，app.root_path 返回程序实例所在模块的路径
（目前来说，即项目根目录），我们使用它来构建文件路径。
下面写入了一个 SQLALCHEMY_DATABASE_URI 变量来告诉 SQLAlchemy 数据库连接地址：
'''
dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.db')

'''
 关闭对模型修改的监控

'''
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
