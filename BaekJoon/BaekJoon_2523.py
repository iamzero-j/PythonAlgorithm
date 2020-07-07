# 출처 : 백준 알고리즘 -> https://www.acmicpc.net/problem/2523


# 별찍기 문제
# N=3 이면 
# *
# **
# ***
# **
# *
# 이런식으로 나타나게 하기

N=int(input())

for i in range(1,N):
    print("*"*i)
for i in range(0,2*N):
    print("*"*(N-i))
