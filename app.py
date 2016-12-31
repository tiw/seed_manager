import flask
from flask import request
from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


#engine = sqlalchemy.create_engine('mysql://root:@localhost/pian', echo=True)
engine = sqlalchemy.create_engine('sqlite:///seeds.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Seed(Base):
    __tablename__ = 'seeds'

    id = Column(Integer, primary_key=True)
    seed = Column(String(200))
    file_name = Column(String(100))

    def __repr__(self):
        return "<Seed(seed:{}, name:{})".format(self.seed, self.file_name)


app = flask.Flask(__name__, static_url_path='/static')
app.secret_key = 'alibabahe4odadao'
admin = Admin(app, name='seed', template_mode='bootstrap3')
admin.add_view(ModelView(Seed, session))


if __name__ == '__main__':
    app.run(debug=True)
