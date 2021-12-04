f = open("input.txt","r")
a = f.readlines()
b=[]
n=0
while n<12:
    ones=0
    zeros=0
    for i in a:
        if i[n]=="1":
            ones+=1
        else:
            zeros+=1
    if ones>zeros:
        b.append("1")
    else:
        b.append("0")
    n+=1
gamma = int(''.join(b),2)
c=[]
for i in b:
    if i=="1":
        c.append("0")
    else:
        c.append("1")
epsilon = int(''.join(c),2)
print(gamma*epsilon)
