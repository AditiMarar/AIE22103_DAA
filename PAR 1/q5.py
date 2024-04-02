def pal(s,i1=0,i2=-1):
    x=len(s)//2
    if x-1==i1:
        return s[i1]==s[i2]
    else:
        return (s[i1]==s[i2])and pal(s,i1+1,i2-1)
s=input("Enter a word~ ")
if pal(s):
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")

