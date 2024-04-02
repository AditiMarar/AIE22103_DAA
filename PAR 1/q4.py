def rev(s,i=-1):
    if i==(-1*len(s)):
        return s[i]
    else:
        return s[i]+rev(s,i-1)
s=input("Enter a string~ ")
print("Reverse of",s,"is~",rev(s))
