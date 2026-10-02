import os
class Config:
    SECRET_KEY = "campus-connect-secret-key"
    SQLALCHEMY_DATABASE_URI ="sqlite:///campus_connect.db"
    SQLALCHEMY_TRACK_MODIFICATIONs =False 
    
    UPLOAD_FOLDER = os.path.join("app","static","uploads")