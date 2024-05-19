from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router.mongo_router import mongo_router
from router.neo4j_router import neo4j_router
from router.analyst_router import analyst_router
import uvicorn
app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(mongo_router)
app.include_router(neo4j_router)
app.include_router(analyst_router)



if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000,reload=True)