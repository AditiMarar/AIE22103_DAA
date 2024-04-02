#q1
n=[8,7,2,5,3,1]
t=10
p=[]
for i in range(len(n)):
    for j in range(len(n)):
        if i!=j:
            if n[i]+n[j]==t:
                if [n[j],n[i]] not in p:
                    p+=[[n[i],n[j]]]
if len(p)==0:
    print("Pair not found")
else:
    for i in p:
        print("Pair found (",i[0],",",i[1],")")
