from werkzeug.utils import secure_filename
from replit import db
import os

# database

def getkeys():
    return db.keys()
