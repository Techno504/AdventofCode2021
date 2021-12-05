f = open("input.txt","r")
a = f.readlines()
nums=[]
boards=[]
board=[]
counter=-1
for i in a:
    if counter==-1:
        nums=i.strip("\n").split(",")
    else:
        if i!="\n":
            board.append(i.split())
        if counter%5==0:
            boards.append(board)
            board=[]
    counter+=1
for i in nums:
    for i in boards[1:]:
        for j in i:
            if str(n) in j:
                # do something
