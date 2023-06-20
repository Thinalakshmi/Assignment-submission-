from pymongo import MongoClient
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")

db = client.interns_b2_23
collection = db.thina
class Emp(BaseModel):
    id: str
    name: str
    password: str
    email: str
    phone_no: str


# Insert an employee
@app.post("/add_employee")
async def add_employee(emp: Emp):
    collection.insert_one(emp.dict())
    return {"message": "employee added successfully"}

@app.get("/read_employee")
async def read_employee(id: str):
    employee=collection.find_one({"id": id})
    if employee:
        return {"id":employee['id'],
                "name":employee['name'],
                "password":employee['password'],
                "email":employee['email'],
                "phone_no":employee['phone_no'],}
    else:
        return {"message": "employee not found"}

@app.put("/update_employee")
async def update_employee(id: str, emp:Emp):
    employee = collection.find_one({"id": id})
    if employee:
        collection.update_one({"id": id},{"$set":emp.dict()})
        return {"message": "employee details updated successfully"}
    else:
        print("employee id found")

@app.delete("/delete_employee")
async def delete_employee(id: str):
    employee = collection.find_one({"id": id})
    if employee:
        collection.delete_one({"id": id})
        return {"message": "employee details removed successfully"}

    else:
        print("record not found")

