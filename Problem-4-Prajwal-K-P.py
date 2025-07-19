def createList():
    l=[]
    while True:
        try:
            n=int(input("Enter the number:"))
            l.append(n)
        except Exception as e:
            break
    return l
def countnumbers(numbers):
    result = {}
    for i in range(1, 10):  
        count = 0
        for num in numbers:
            if num % i == 0:
                count += 1
        result[i]=count
    return result
numbers=createList()
res=countnumbers(numbers)
print(res)
