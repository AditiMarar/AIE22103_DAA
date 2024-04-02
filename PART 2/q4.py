#q5
x=[[1,4],[2,5],[7,8],[6,9]]
o=[]
print("Set of activities")
print(x)
while len(x)!=0:
    y=x.pop(0)
    m=y[1]
    l=[y]
    ind=[]
    for i in range(len(x)):
        if x[i][0]>m:
            l+=[x[i]]
            m=x[i][1]
            ind+=[i]
    for i in range(len(ind)-1,-1,-1):
        x.pop(ind[i])
    o+=[l]
print("Output")
print(o)
