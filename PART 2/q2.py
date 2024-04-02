x=[[10,20,30,40],[32,33],[27,29,37,48,93],[15,25,35]]
m=0
a=x.pop(0)
o=[a]
while len(o)!=4:
    b=x.pop(0)
    for i in range(len(o)):
        if i==len(o):
            o.append(b)
        elif o[i][0]<b[0]:
            o.insert(i,b)
for i in range(3,-1,-1):
    print(o[i])
