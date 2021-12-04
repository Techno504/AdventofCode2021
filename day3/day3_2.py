f = open("input.txt","r")
a = f.readlines()


oxy_list=[]
co2_list=[]

for i in a:
    oxy_list.append(i.strip("\n"))
    co2_list.append(i.strip("\n"))

def loop(nums):
    n=0
    while n<12:
        ones,zeros=0,0
        #oxy_ones,oxy_zeros,co2_ones,co2_zeros=0,0,0,0

        for i in a:
            if i[n]=="1":
                ones+=1
            else:
                zeros+=1

        # for i in oxy_list:
        #     if i[n]=="1":
        #         oxy_ones+=1
        #     else:
        #         oxy_zeros+=1
        # for i in co2_list:
        #     if i[n]=="1":
        #         co2_ones+=1
        #     else:
        #         co2_zeros+=1

        if ones>zeros:
            for i in oxy_list:
                if i[n]!="1":
                    oxy_list.remove(i)
            for i in co2_list:
                if i[n]!="0":
                    co2_list.remove(i)

        elif zeros>ones:
            for i in oxy_list:
                if i[n]!="0":
                    oxy_list.remove(i)
            for i in co2_list:
                if i[n]!="1":
                    co2_list.remove(i)

        elif zeros==ones:
            for i in oxy_list:
                if i[n]!="1":
                    oxy_list.remove(i)
            for i in co2_list:
                if i[n]!="0":
                    oxy_list.remove(i)


        # if co2_zeros>co2_ones:
        #     for i in co2_list:
        #         if i[n]!="1":
        #             co2_list.remove(i)
        # elif co2_ones<=co2_zeros:
        #     for i in co2_list:
        #         if i[n]!="0":
        #             co2_list.remove(i)

        b=oxy_list+co2_list
        b=list(dict.fromkeys(b))
        n+=1

b=a
while len(oxy_list)>1 or len(co2_list)>1:
    loop(b)
print(oxy_list)
print(co2_list)
