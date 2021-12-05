f = open("input.txt","r")
a = f.readlines()
b=[]
grid=[]
count=0
n=0
for i in range(501):
    row=[]
    for i in range(1001):
        row.append(0)
    grid.append(row)
for i in a:
    b.append(i.strip("\n").split(" -> "))
for i in b:
    if i[0].split(",")[0] == i[1].split(",")[0]:
        x,y=int(i[0].split(",")[1]),int(i[1].split(",")[1])
        for i in range(min(x,y),max(x,y)+1):
            if grid[n][i]==0:
                grid[n][i]=1
            elif grid[n][i]==1:
                grid[n][i]=2
                count+=1
            elif grid[n][i]==2:
                grid[n][i]=3
                count-=1
    elif i[0].split(",")[1] == i[0].split(",")[1]:
        x,y=int(i[0].split(",")[0]),int(i[1].split(",")[0])
        for i in range(min(x,y),max(x,y)+1):
            if grid[n][i]==0:
                grid[n][i]=1
            elif grid[n][i]==1:
                grid[n][i]=2
                count+=1
            elif grid[n][i]==2:
                grid[n][i]=3
                count-=1
    n+=1
print(grid)
