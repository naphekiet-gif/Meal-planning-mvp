from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    created_at: str


class Meal(BaseModel):
    id: int
    name: str
    user_id: int
    date: str


class Recipe(BaseModel):
    id: int
    title: str
    ingredients: list[str]
    instructions: str


class ShoppingList(BaseModel):
    id: int
    user_id: int
    meals: list[Meal]
    created_at: str