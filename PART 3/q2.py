#q2
a=[1,7,4,2,8,6,3,9,5]
max1=a[0]
max2=a[0]
for i in range(1,len(a)):
    if a[i]>max1:
        max1=a[i]
for i in range(1,len(a)):
    if a[i]>max2 and max1>a[i]:
        max2=a[i]
print("Maximum product is",max1,"*",max2,"=",max1*max2)
