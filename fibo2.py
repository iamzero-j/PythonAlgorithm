#피보나치 반복적 방법
def fibo(x):
    re0=0
    re1=1
    if(x==0): return 0
    elif(x==1): return 1
    else:
        for i in range(1,x):
            re2=re0+re1
            re0=re1
            re1=re2

        return re2
x=10
print(fibo(x))
