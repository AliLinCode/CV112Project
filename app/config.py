import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://user:password@mariadb:3306/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
