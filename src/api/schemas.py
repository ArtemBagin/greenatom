from pydantic import BaseModel


class StartScheme(BaseModel):
    start_number: int
