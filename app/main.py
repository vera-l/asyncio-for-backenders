from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import ORJSONResponse

from app.core import auth
from app.routes import views


@app.get('/')
async def root(vera: int):
    return {
        'message': 'Hello World',
    }

app = FastAPI(
    title='Asyncio for backenders',
    description='An example app',
    version='1.0.0',
    default_response_class=ORJSONResponse,
)

@app.on_event('startup')
async def connect():
    pass

@app.on_event('shutdown')
    async def shutdown():
        pass

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/static', StaticFiles(directory='app/static'), name='static')
app.include_router(auth.router)
app.include_router(views.router)
