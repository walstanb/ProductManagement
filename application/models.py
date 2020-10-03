import flask
from application import app, db
from werkzeug.security import generate_password_hash, check_password_hash
'''
class team_schedule(db.Document):
    Id          = db.StringField()
    Date        = db.StringField()
    Time        = db.StringField()
    HomeTeam    = db.StringField()
    AwayTeam    = db.StringField()

class account_status(db.Document):
    cid = db.IntField( primary_key=True )
    aid = db.IntField()
    account_type = db.StringField( max_length=50 )
    status = db.StringField( max_length=50 )
    message = db.StringField( max_length=100 )
    last_updated = db.StringField( max_length=100 )
   ''' 