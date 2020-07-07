# 출처 : 백준 알고리즘 -> https://www.acmicpc.net/problem/2884
# 원래 시간 보다 45분 앞 시간

hour, minute = map(int, input().split())
if minute<45:
    minute += 15
    if hour == 0:
        hour += 23
    else:
        hour -= 1
    print(hour, minute)
else:
    minute -= 45
    print(hour, minute)


