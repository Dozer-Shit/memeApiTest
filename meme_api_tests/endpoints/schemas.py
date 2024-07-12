from pydantic import BaseModel


# class ObjInfo(BaseModel):
#     title: str
#     type: str


class ResponseSchema(BaseModel):
    id: int
    info: object
    tags: list
    text: str
    updated_by: str
    url: str


class TokenGetResponseSchema(BaseModel):
    token: str
    user: str


class ResponseSchemaAll(BaseModel):
    data: list[ResponseSchema]
