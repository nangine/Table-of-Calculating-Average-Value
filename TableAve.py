A=[1,2,3,4,5,6,7,8,9,10]
X=[11.7,11.8,11.9,12.0,12.0,12.1,12.1,12.2,12.3,12.3]

def ave (X):
    return (sum (X)/float(len(A)))

print ()
print ()
print ("Data Table")
print("Num.  ","   X     ","   X-Xr   ")
for i in range (0,len(A)):
    print ((A[i]),"     ",(X[i]),"     ",round((X[i]-ave(X)),2))
print ()
print ("X rata-rata = ",round(ave(X),2))
print ()
