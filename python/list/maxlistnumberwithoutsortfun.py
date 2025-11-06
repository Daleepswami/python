mylist=[10,20,30,40]
max=0
for i in range(0,len(mylist)):
    if (max < mylist[i]):
        max=mylist[i]
print( i,max)
