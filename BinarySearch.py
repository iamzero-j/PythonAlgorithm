#리스트 L과 그 안에서 찾으려하는 원소 X가 인자로 주어질 때 X와 값은 값 리턴, 존재하지 않을 경우 -1

def solution(L, x):
    lower=0
    upper=len(L)-1
    while(lower<=upper):
        middle=(lower+upper)//2
        if(L[middle]==x):
            return middle
        elif(L[middle]>x):
            upper=middle-1
        else: # L[middle]<x
            lower=middle+1

    if x not in L:
        return -1
L=[2,3,5,6,9,11,15]
x=6
print(solution(L,x))
