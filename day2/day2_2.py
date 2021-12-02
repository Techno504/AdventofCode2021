f = open("input.txt","r")
a = f.readlines()
vertical=0
horizontal=0
aim=0
for i in a:
    b=i.split()
    if b[0]=="forward":
        horizontal+=int(b[1])
        vertical+=(aim*int(b[1]))
    elif b[0]=="up":
        aim-=int(b[1])
    else:
        aim+=int(b[1])
print(vertical*horizontal)
