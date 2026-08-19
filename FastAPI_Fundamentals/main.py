from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return({'Message':"Hello, Worlds!"})

@app.get('/about')
def index():
    return("KabirTech Solutions is an initiative startup who claims on the slogans of Innovating Technologies, Empowering Growth")

@app.get("/cal")
def calculator(num1:int, operator:str, num2:int):
    #num1 = int(input('Enter the nujmber: '))
    #operator = input("Enter the operator: (+,-,/,//,%)")
    #num2 = int(input('Enter the nujmber: '))
    dic = {'+':num1+num2,'-':num1-num2,'*':num1*num2,'/':num1/num2,'%':num1%num2}
    return dic[operator]

