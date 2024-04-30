user_input = input("Enter a list of elements separated by commas: ")
user_input=[]
k=int(input(""))
l1=[]
max1=[]
for i in range(len(user_input)):
    l1.append(i)
    l1.append(i+1)
    l1.append(i+2)
    max1=max(l1)
print(max1)   
    