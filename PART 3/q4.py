#Q4
i_ar=[]
i=input("Enter 0 or 1: ")
while i!="":
    if int(i)==0 or int(i)==1:
        i_ar+=[int(i)]
    else:
        print("Wrong no. enter again")
    i=input("Enter 0 or 1: ")
print("Input array: ",i_ar)
for i in range(0,len(i_ar)):
    if i_ar[i]==0:
        temp=i_ar.pop(i)
        i_ar.insert(0,temp)
print("Output array: ",i_ar)
