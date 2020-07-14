# 출처 : 백준 -> 문자열 : 공백 없이 주어신 숫자 N개의 합 - 11720번 
# https://www.acmicpc.net/problem/11720

#첫째 줄 : 숫자의 개수 N (1 이상 100 이하)
#둘째 줄 : 숫자 N개가 공백 없이 주어짐
#출력 : 주어진 숫자 N개의 합

N=int(input())
ins=list(input())

print(ins)
print(sum(map(int,ins)))
