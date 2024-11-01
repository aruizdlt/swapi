from fastapi import FastAPI

from app.routes.people_route import router as people_router

app = FastAPI()

app.include_router(people_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Star Wars API using Clean Architecture!"}
