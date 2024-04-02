import random
def srt_ar(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
x=[random.randint(1,50) for i in range(random.randint(1,30))]

k=31
print("Enter a no. less than ",len(x),", if you don't you'll have to enter again")
while k>len(x):
    k=int(input("Enter a no. "))
a=srt_ar(x)
print(x)
print("The",k,"th largest no. in the list is ",a[-k])
