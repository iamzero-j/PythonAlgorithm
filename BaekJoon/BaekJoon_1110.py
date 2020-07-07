#출처 : 백준 알고리즘 -> 1110번 문제
# -- https://www.acmicpc.net/submit/1110

# N이 다시 N이 될 때까지의 사이클 )
# 십의자리 + 일의 자리 => 일의 자리*10 + (십의자리+일의자리) ..... : 십의자리+일의자리의 합이 10이 넘으면 %10 해서 나머지만 사용

# 예) 26 => 2+6=8 => 68 => 6+8=14 => 84 => 8+4=12 => 42 => 4+2=6 => 26
N = int(input())
ins=N # 다시 N이 될 때 비교

cycle = 0 # 사이클 수

while True:
    ten = N // 10  #십의 자리 
    one = N % 10 # 일의 자리
    result = ten + one # 십의자리+일의자리
    cycle += 1
    N = int(str(N%10) + str(result%10)) #십의자리와 일의자리의 합이 10이상 되지 않게 함

    if (ins == N): #사이클 하면서 N의 값이 ins와 같아질 때 멈춤
        break
print(cycle)
