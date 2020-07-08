# 출처 : 백준 -> 2446번 : https://www.acmicpc.net/problem/2446

#별찍기 - 모래시계 모양 

N=int(input())

for i in range(0,N): 
    print(" " * i, end="")
    print("*" * ((2*N-1)-(2*i)))
    
for j in range(N-2,-1,-1):
    print(" " * j, end="")
    print("*" * ((2*N-1)-(2*j)))
