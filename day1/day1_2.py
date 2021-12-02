f = open("input.txt","r")
a = f.readlines()
c=0
counter=0
increases=0
for i,j,k in zip(a,a[1:],a[2:]):
    b=int(i)+int(j)+int(k)
    if counter!=0 and b>c:
        increases+=1
    counter+=1
    c=b
print(increases)
