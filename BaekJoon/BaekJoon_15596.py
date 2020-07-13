#출처 : 백준 -> 함수 : https://www.acmicpc.net/problem/15596

#정수가 N개, N개의 합을 구하는 함수

#방법1 : 단순 무식하게 for문으로 구하기
def solve(a:list):
    #a : 합을 구해야 하는 정수 n개가 저장되어 있는 배열
    #a=[1,2,3,4,5]
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    return sum

#방법2 
def solves(a:list):
    result=sum(a)
    return result

a=[1,2,3,4,5]
print(solve(a))
print(solves(a))
