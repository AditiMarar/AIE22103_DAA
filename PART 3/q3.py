#q3
a=[3,8,6,7,5,9]
print("Original matrix~ ",a)
l=[]
for i in range(0,len(a)):
    if i!=len(a)-1:
        if a[i]>a[i+1]:
            l+=[i]
x=a[l[0]]
a[l[0]]=a[l[1]+1]
a[l[1]+1]=x

print("Matrix after swapping~ ",a)
