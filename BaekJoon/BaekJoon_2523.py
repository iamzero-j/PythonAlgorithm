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
for i in range(N):
    print("*"*i)
for i in range(2*N-N):
    print("*"*(N-i))

# 파이참에서는 잘 돌아가는데 백준 제출하면 출력형식이 잘못되었습니다 나옴 
