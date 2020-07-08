#출처 : 백준 -> 1차원 배열 : https://www.acmicpc.net/problem/10818

#10818번 : 최대 최소값
# N = 5 이면 X 5개 받아서 최대,최소값 구하기 
N=int(input())
x=list(map(int, input().split()))
print(min(x),end=" ")
print(max(x))

#이렇게 풀면 굳이 N이 필요 없음.. --> min(), max() 대신 직접 for문으로 순차정렬하기 
