#정렬 문제
#프로그래머스 - [K번째수]
#문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42748
#배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 한다.
# array=[1,5,2,6,3,7,4] i=2,j=5,k=3  ==> [5,2,6,3] -> 정렬 : [2,3,5,6] => 3번째 숫자 =5
# 이차원 배열 [[i,j,k]] 로 반환.

def solution(array,commands):
    temp=[[]]
    arrays=[[]]
    for x in range(len(commands)):

        arrays=array[int(commands[x][0]-1):int(commands[x][1])]

        arrays.sort()
        print(str(x)+"번째 ) ")
        print(arrays)
        temp.append(int(arrays[commands[x][2]-1]))
        print(int(arrays[commands[x][2]-1]))
    temp.remove([])
    return temp
