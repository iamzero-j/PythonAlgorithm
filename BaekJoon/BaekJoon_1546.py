# 출처 : 백준 - 1차원 배열 1546번 -> https://www.acmicpc.net/problem/1546

# N= int(input()) - 시험 본 개수 // grade=N개 입력 받음 --> 각각의점수/최고점*100으로 새로운 점수를 구한 다음 평균 구하기

N=int(input())

grade=list(map(int,input().split()))
mx=max(grade)
re=[]
for i in range(N):
    re.append(int(grade[i])/mx*100)

print(sum(re)/len(re))
