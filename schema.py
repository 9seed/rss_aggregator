from pydantic import BaseModel


class News(BaseModel):
    title: str
    id: str
    link: str
    author: str
    updated: str
    summary: str
    content: str

    class Config:
        orm_mode = True