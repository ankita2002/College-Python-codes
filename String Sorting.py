print("*************String Sorting*****************")
n = int(input("Enter the length of Array: "))
print("Enter ",n,"elements in the array: ")
strs = ["" for _ in range(n)]
x =[]
for i in range(0,n):
    x.append(input("Enter String Value: "))
print("Input Array: ",x) 
x.sort()
for i in range(0,n):
    strs[i]=x[i]
print("Array after sorting: ", strs)
