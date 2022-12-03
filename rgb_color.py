from pydantic import BaseModel


class RGBColor(BaseModel):
    r: int
    g: int
    b: int
