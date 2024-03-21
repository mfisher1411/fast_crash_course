# This is a sample Python script.
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('Database is cleard')
    await create_tables()
    print('Database is ready for use')
    yield
    print('Shutting down')
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)





