# 출처 : 백준 -> 함수 : 1065번 https://www.acmicpc.net/problem/1065

# 어떤 양의 정수 x의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
==> 예)321 은 -1씩 차이나는 등차수열 (3-2) == (2-1) or (2-3)==(1-2)

# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수 출력
# N의 범위 = 1~1000
#예) 110 --> 99개 // 1 --> 1개 // 210 --> 105개 // 1000-->144개

def d(N):
    count=0
    if(N<100): return N
    elif(N<1001):
        for i in range(100,(N+1)): #100~1001이하의 수
            x=(i//100) #백의 자리
            y=((i%100)//10) #십의 자리
            z=((i%100)%10) #일의 자리

            if(x-y==y-z): # d 크기
                count+=1
        return count+99
        
     #1001부터는 None값
     
N=int(input())
print(d(N))
