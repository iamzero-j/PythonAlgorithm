#출처 : 백준 -> 1차원 배열 : https://www.acmicpc.net/problem/10818

#최대 최소값
# N = 5 이면 X 5개 받아서 최대,최소값 구하기 
N=int(input())
x=list(map(int, input().split()))
print(min(x),end=" ")
print(max(x))
