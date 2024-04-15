def min_candy(l):
    c=[1]
    for i in range(1,len(l)):
        if l[i]>l[i-1]:
            c+=[c[i-1]+1]
        else:
            if c[i-1]>3:
                c+=[c[i-1]-2]
            else:
                c+=[c[i-1]-1]       
    return c
def result(l):
    s=sum(l)#s is for sum
    od=""#od if for optimal distribution
    for i in l:
        od+=str(i)
    return s,od
print("Enter no.s, first no. will be the size of the array")
n=int(input(""))
l=[]
for i in range(n):
    ele=int(input(""))
    l+=[ele]
c=min_candy(l)
r=result(c)
print("Optimal distribution will be~",r[1])
print("Total candies required for miss alice's class is",r[0])
