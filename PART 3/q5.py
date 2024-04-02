#q5
a=[10,1,2,4,13,9,5]
l=[]
for i in range (len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            l+=[[a[i],a[j]]]
print("The inversions are~\n",l)
print("Total no. if inversions are",len(l))
