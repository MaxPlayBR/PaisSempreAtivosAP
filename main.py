from app import app, db
from models import User,Medias
import requests,json

@app.shell_context_processor
def shell_context():
    return dict(
        app=app,
        db=db,
        User=User,
        Medias=Medias
    )
    
if __name__ == '__main__':
    app.run()
