# 리스트 x의 첫 원소와 마지막 원소의 합을 리턴하는 함수

def solution(x):
    sum=x[0]+x[-1] # 또는 x[0]+x[len(x)-1]
    return sum

x=[5,3,8,2]

print(solution(x))
