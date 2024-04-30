l = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

length=len(l)
new_l=[]
i=0
k=int(input("Enter partition limit: "))
sum=[]
while i<length:
    for j in range(0,k):
        new_l.append(l[i])
        i+=1
    print(new_l,"-->",max(new_l))
    new_l.clear()