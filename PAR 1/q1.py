import matplotlib.pyplot as plt
def sum_n(x):
    if x==1:
        return 1
    else:
        return sum_n(x-1)+x
n=int(input("Enter a no. "))
x=[i for i in range(1,n+1)]
y=[sum_n(i) for i in range(1,n+1)]
plt.title("n vs sum of n integers")
plt.plot(x,y,marker="o")
plt.show()
