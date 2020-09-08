#출처 : 백준 -> 정렬:   https://www.acmicpc.net/problem/1427

#1427번 : 숫자를 입력 --> 자릿수를 내림차순으로 출력

# N=1427 이면 출력은 7241 

import sys

n=list(map(str,sys.stdin.readline()))
n.remove('\n')

n.sort(reverse=True)
for i in range(len(n)):
    print(n[i],end='')
