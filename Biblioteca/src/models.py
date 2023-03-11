from typing import Optional

from sqlmodel import Field, SQLModel


class Libro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    isbn: str
    paginas: Optional[int] = None
