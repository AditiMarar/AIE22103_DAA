#q6
n=[8,7,2,5,3,1]
t=10
p=[]
print("When time complexity is O(n^2)")
for i in range(len(n)):
    for j in range(len(n)):
        if n[i]+n[j]==t:
            if [n[j],n[i]] not in p:
                p+=[[n[i],n[j]]]
if len(p)==0:
    print("NO")
else:
    for i in p:
        print("YES")

print("When time complexity is O(nlog(n))")
P=[]
for i in range(len(n)):
    j=0
    while j<len(n):
        if n[i]+n[j]==t:
            if [n[j],n[i]] not in p:
                P+=[[n[i],n[j]]]
        j+=1
if len(P)==0:
    print("NO")
else:
    for i in P:
        print("YES")
