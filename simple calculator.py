n=int(input("enter the number of entries "))
for j in range(n):
    str=input()
    count=0
    for i in range(len(str)):
        if str[i].isnumeric()!=True:
            count=i
    number1=int(str[0:count])
    number2=int(str[count+1:len(str)])
    if str[count]=='+':
        print(number1+number2)
    elif str[count]=='-':
        print(number1-number2)
    elif str[count]=='*':
        print(number1*number2)
    elif str[count]=='/':
        print(number1/number2)
    elif str[count]=='%':
        print(number1%number2)
    else:
        print("invalid number")



