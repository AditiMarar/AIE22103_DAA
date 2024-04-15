def m_s(l):#m_s stands for maximum sum given by the array
    l.sort()#sorting l
    s=0#sum
    for i in range(len(l)):
        s+=l[i]*i
    return s
x=[2,5,3,4,0]
total=m_s(x)
print("Maximum sum of",x,"is~",total)
