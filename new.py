l = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

length=len(l)
new_l=[]
i=1
k=int(input("Enter partition limit: "))
sum=[]
new_l.append(l[0])
while i<length:
    for j in range(1,k):
        new_l.append(l[i])
        i+=1
    print(new_l,"-->",max(new_l))
    b=new_l[k-1]
    new_l.clear()
    new_l.append(b)