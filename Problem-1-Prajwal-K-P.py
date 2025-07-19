def calculator(a,b,operation):
    operation=operation.lower()
    if operation == "add":
        return a+b
    elif operation =="subtract":
        return a-b
    elif opeartion =="multiply":
        return a*b
    elif operation =="divide":
        if b!=0:
            return a/b
        else:
            print("Not Defined")
    else:
        print("Invalid Input")
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
operation=input("Enter the operation type:")
res=calculator(a,b,operation)
print(res)
