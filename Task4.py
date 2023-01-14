"""
Write a program for Fibonacci numbers
"""
n1 = 0 #first term
n2 = 1 #second term
nterm = int(input("Enter the no. of term for fibonacci series:"))

if nterm==1:
    print(n1)
else: 
    print("1 st term :",n1)
    print("2 nd term :",n2)
    count = 3
    while count <= nterm:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        if(n3==3):
            print("3 rd term :",n3)
            continue
        print(count,"th term :",n3)
        count += 1
        
