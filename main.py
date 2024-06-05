from fastapi import FastAPI, Query, Path
from typing import Optional, Annotated
from pydantic import BaseModel

app = FastAPI()

""" Task 1: Basic Query Parameters
Create an endpoint that accepts multiple query parameters and returns them in a structured format
"""
@app.get("/items/")
def get_items(name:str, category:str, price:float):
    return {"name":name, "category":category, "price":price}


""" Task 2: Query Parameters with Default Values and Optional Fields
 Create an endpoint that uses query parameters with default values and optional fields.
"""
@app.get("/search/")
def search_item(query:Optional[str] = "abc", page:Optional[int] = 1, size:Optional[int] = 10):
    return {"query":query, "page":page, "size":size}


""" Task 3: Request Body with Nested Pydantic Models
Create an endpoint that accepts a complex JSON request body with nested Pydantic models.
"""
class Address(BaseModel):
    street: str
    city: str
    zip: int
    
class User(BaseModel):
    name: str
    email: str
    address: Address
    
@app.post("/users/")
def user(user: User):
    return {"user_info": user}

""" Task 4: Query Parameters with String Validations
Create an endpoint that validates query parameters using string validations that includes length and regex.
"""
#regex that validate if the first letter of the username is a capital letter
@app.get("/validate/")
def validate_username(username: Annotated[str, Query(min_length=2, max_length=20, regex="[A-Z].+")]):
    return {"message": f"The username '{username}' is valid!"}

""" Task 5: Combined Parameters and Validations
Create an endpoint that combines path parameters, query parameters, and request body with validations.
"""
class Report(BaseModel):
    title: str
    content: str
    
@app.post("/reports/{report_id}")
def reports(report_id:int = Path(gt=0),*, state_date:str, end_date:str, report:Report):
    return {"report_id":report_id, "state_date": state_date, "end_date": end_date, "report":report}