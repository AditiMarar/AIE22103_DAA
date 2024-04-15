def min_s(x,y): #find minimum sum of lists x and y
    #assuming both are of same length
    x.sort()
    y.sort()
    ms=0
    for i in range(len(x)):
        iy=-1*(i+1)#index for y
        ms+=x[i]*y[iy]
    return ms
a=[7,5,1,4]
b=[6,17,9,3]
print("A=",a)
print("B=",b)
mins=min_s(a,b)
print("the minimum sum A & B is~",mins)
