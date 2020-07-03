# 리스트 L과 정수 X가 인자로 주어질 때 X를 올바를 위치에 삽입 --> 반환
# 가정 : 리스트 L이 오름차순으로 정렬되어 있다고 가정

def solution(L, x):
    ans = []
    index = 0

    for i in range(len(L)):
        if (L[0] > x):
            index = 0
            break
        elif (L[i] < x):
            index = i

    if (index == 0 and x < L[0]):
        L.insert(0, x)
    else:
        L.insert(index + 1, x)
    ans=L
    return ans

L=[20,37,58,72,91]
x = 65

print(solution(L,x))
