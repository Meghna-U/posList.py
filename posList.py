list=[]
s=int(input("Enter number of elements in list:"))
print("Enter elements of list:")
for x in range(0,s):
    element=int(input())
    list.append(element)
for a in list:
    if a>0:
        print(a)
