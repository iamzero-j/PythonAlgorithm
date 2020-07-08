#출처 : 백준 -->  https://www.acmicpc.net/problem/2562

#2562번 : 수 9개 입력 ==> 9개 중 최대값과 최대값 위치

li=[]
for i in range(0,9):
    x=int(input())
    li.append(x)
print(max(li),end=" ")
print(li.index(max(li))+1)


