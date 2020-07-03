def linear_search(L,x):
    i=0
    while(i<len(L)and L[i]!=x):
        i+=1
    if(i<len(L)):
        return i
    else:
        return -1

L=[9,10,22,3,5,6]
print(linear_search(L,5))
