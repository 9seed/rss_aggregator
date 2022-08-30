import os
import json
import time
from multiprocessing import Pool

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from sqlalchemy.dialects.postgresql import JSON
from utils.rss_aggregator import RssAggregatorService

from models import News
from models import News as ModelCharacter
from schema import News as SchemaCharacter

load_dotenv(".env")

app = FastAPI(title='RSS API', version='1.0.0')

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get("/", tags=["hello"])
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/rss/news/", tags=["News"])
def get_character_sheets(key_word: str):
    news = db.session.query(News).filter(key_word in getattr(News, 'title')).all()
    return news


@app.post("/api/v1/rss/news/", response_model=SchemaCharacter, tags=["News"])
def add_character_sheet(news: SchemaCharacter):
    res = ModelCharacter(title=news.title,
                         id=news.id,
                         link=news.link,
                         author=news.author,
                         updated=news.updated,
                         summary=news.summary,
                         content=news.content)
    db.session.add(res)
    db.session.commit()
    return news


if __name__ == "__main__":
    # p = Pool()
    # host = "0.0.0.0"
    # port = 8000
    # cli = RssAggregatorService()
    # p.apply_async(uvicorn.run, args=(app, host, port))
    # p.apply_async(cli.check_init)
    # p.close()
    # p.join()
    # print('All done')
    # while True:
    #     time.sleep(1)
    uvicorn.run(app, host="0.0.0.0", port=8000)