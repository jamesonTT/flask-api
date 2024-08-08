import os

class Config:
    APP_HOST=os.environ['APP_HOST']
    APP_PORT=os.environ['APP_PORT']
    APP_DEBUG_MODE=os.environ['APP_DEBUG_MODE']