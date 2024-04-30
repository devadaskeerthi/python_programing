l=[1,2,3,4,5,6,7,8,9]
length=len(l)
new_l=[]
i=0
k=3
sum=0
while i<length:
    for j in range(0,k):
        new_l.append(l[i])
        i+=1
        
    sum+=max(new_l)
    new_l.clear()
print(sum)