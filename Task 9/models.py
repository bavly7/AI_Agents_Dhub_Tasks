from pydantic import BaseModel, Field



class BookingDetails(BaseModel):
    hall_name: str = Field(description="The exact name of the hall to book")
    date: str = Field(description="The date for the wedding (e.g., 2026-10-15)")
    customer_name: str = Field(description="The name of the customer booking the hall")

class SearchHallsInput(BaseModel):
    capacity: int = Field(description="Exact guest count as an integer.")
    style: str = Field(description="Preferred style.")
    food: str = Field(description="Food preferences as a single string.")