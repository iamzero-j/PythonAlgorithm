# 출처 : 백준 -> 정렬 : 1181번 https://www.acmicpc.net/problem/1181
# 단어 정렬 : 알파벳 소문자로 단어 n개 입력
# 조건1) 길이가 짧은 것 부터 / 조건2) 길이가 같으면 사전 순

import sys

n=int(input())
x=list()

for i in range(n):
    x.append(sys.stdin.readline().strip())

for i in range(len(x)):
    for j in range(i):
        if len(x[i])<len(x[j]):
            x[i],x[j]=x[j],x[i]
        elif len(x[i])==len(x[j]): #ord()
            a=x[i]
            b=x[j]
            for k in range(len(x[i])):
                if(ord(a[k])<ord(b[k])): # ord() : 아스키코드로 변환 후 비교
                    x[i],x[j]=x[j],x[i]

print(x)
