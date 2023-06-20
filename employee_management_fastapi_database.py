from pymongo import MongoClient
from pydantic import BaseModel
from fastapi import FastAPI, Request

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
db = client.interns_b2_23
collection = db.thina

class Employee(BaseModel):

    username: str
    password: str
    email: str
    phone_no: str

# Insert an employee
@app.post("/emp_signup")
async def emp_signup(request: Request):
    data = await request.form()
    employee = Employee(
        username=data["username"],
        password=data["password"],
        email=data["email"],
        phone_no=data["phone_no"],
    )
    collection.insert_one(employee.dict())
    return {"message": "Sign up page created successfully"}
@app.post("/emp_login")
async def emp_login(request: Request):
    data = await request.form()
    username=data["username"]
    password = data["password"]
    employee=collection.find_one({"username":username,"password":password})
    if employee:
        return {"message": "login  Successfull"}
    else:
        return{"error":"Login failed,username or password is wrong!!"}
@app.post("/emp_update")
async def emp_update(request: Request):
    data = await request.form()
    username = data["username"]
    password = data["password"]
    new_password = data["new_password"]
    employee = collection.find_one({"username": username})
    if employee:
        employee["password"] = new_password
        collection.update_one({"username": username}, {"$set": employee})
        return {"message": "Employee details updated successfully"}
    else:
        return {"error": "Employee username not found"}


@app.post("/emp_delete")
async def emp_delete(request: Request):
    data = await request.form()
    username = data["username"]
    employee = collection.find_one({"username": username})
    if employee:
        collection.delete_one({"username": username})
        return {"message": "employee details removed successfully"}
    else:
        return {"error": "employee record not found"}


# Run the FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=5001)