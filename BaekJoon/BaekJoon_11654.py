#출처 : 백준 --> 문자열 : 11654번 - N의 아스키코드값?
# https://www.acmicpc.net/problem/11654

#방법1)
N=input()
ac=0

uppers='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowers='abcdefghijklmnopqrstuvwxyz'
num='0123456789'

if(N.isupper()):
    ac=65
    for i in range(len(uppers)):
        if(N==uppers[i]):
            ac+=i
elif(N.islower()):
    ac=97
    for i in range(len(lowers)):
        if(N==lowers[i]):
            ac+=i
else:
    ac=48
    for i in range(len(num)):
        if(N==num[i]):
            ac+=i

print(ac)

#방법2
N=input()
print(ord()) #ord() 는 아스키코드값을 나타내줌
