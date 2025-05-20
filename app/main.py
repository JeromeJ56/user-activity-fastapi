from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session
from .database import engine,get_db
from .import models
from fastapi.middleware.cors import CORSMiddleware
# from .config import settings

# print(settings.database_username)
# we can resues this command if we are not using alembic
models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="User activity")
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/user/{username}>/activity/")
def record_activity(username : str,db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username==username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Username {username} does not exist")
    new_activity = models.User(user_id=user.id, activity_type=user.username, timemstamp=user.timestamp,meta_data = user.meta_data)
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)
    return {"message":"activity recorded"}
    
