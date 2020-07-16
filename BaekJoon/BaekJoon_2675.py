# 출처 : 백준 - 문자열 : 2675번

# https://www.acmicpc.net/problem/2675

# 테스트 케이스 T --> 반복횟수 R, 문자열 S : r = 공백으로 구분
T=int(input())

for i in range(T):
    a,b=input().split(' ')
    a=int(a)
    for j in range(len(b)):
        print(b[j]*a,end='')
    print()
