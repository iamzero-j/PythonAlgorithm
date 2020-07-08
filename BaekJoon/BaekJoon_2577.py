# 출처 : 백준 -> 1차원 배열 2577번 : https://www.acmicpc.net/problem/2577

# a*b*c -> 0~9까지의 숫자 몇 개가 쓰였는가
a=int(input())
b=int(input())
c=int(input())

muti=a*b*c
li=list(str(muti))
print(li)


for i in range(10):
    print(li.count(str(i)))
