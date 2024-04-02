def num_str(n,i=0):
    if len(n)-1==i:
        return n[i]
    else:
        x=len(n)-i-1
        if x%3==0:
            return n[i]+","+num_str(n,i+1)
        else:
            return n[i]+num_str(n,i+1)
n=input("Enter a no. ")
print("Representation~",num_str(n))
