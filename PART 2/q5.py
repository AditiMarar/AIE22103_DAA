#q5
def min_max_merge(l):
    mmin=l[0][0]
    mmax=l[0][1]
    for i in l:
        if i[0]<mmin:
            mmin=i[0]
        if i[1]>mmax:
            mmax=i[1]
    return [mmin,mmax]
x=[[1,4],[2,5],[7,8],[6,9]]
o=[]
print("Set of intervals")
print(x)
while len(x)!=0:
    y=x.pop(0)
    l=[y]
    ind=[]
    m=0
    for i in range(len(x)):
        if x[i][0]<y[1]:
            l+=[x[i]]
            ind+=[i]
    for i in ind:
        x.pop(i)
    o+=[min_max_merge(l)]
print("After merging")
print(o)
