
from fastapi import FastAPI
app = FastAPI()
#it will create a object of fastApi


@app.get("/add")      #define a path operation decorator
async def add(num1:int,num2:int):   #define the path operation function
    return {"the addition of two number is": num1+num2}


@app.get("/sub")
async def sub(num1:int,num2:int):
    return {"the subtraction of two number is": num1-num2}


@app.get("/mul")
async def mul(num1:int, num2:int):
    return {"the multiplication of two number is": num1*num2}


@app.get("/div")
async def div(num1:int,num2:int):
    if num2!=0:
        return {"the division of two number is": num1/num2}
    else:
        return {"division is not possible"}


@app.get("/mod")
async def mod(num1:int,num2:int):
    return {"the modulo of two number is": num1%num2}