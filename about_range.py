
y = 5
for x in range(6):
    print(" "*y,'*'*x)
    y -= 1

a = [90, 25, 67, 45, 80]
n = 0
for mark in a:
    n += 1
    if mark < 60: continue #continue는 for 문으로 들어가는 데 일을 안하는거, break은 탈주
    print("%d번 학생은 합격임"%n)

for _ in range(100): #range는 0번부터 시작해서 n - 1번을 출력함 --> 0부터 99번까지 출력
     print(_)

for _ in range(1,11): print(_) #1번부터 10번까지 출력

for i in range(0,10,2) : #0 부터 10-1까지 2단위로 출력해봐
    print(i)

for i in range(10,0) : print(i) #range는 더하기라 이러면 작동안함

for i in range(10,0,-1) : print(i) #<_ 이래야 나옴

count = int(input("반복할 수를 입력 : "))
for i in range(count): print("hello world!",i)

s = 0
for i in range(1,11):
    s = s + i
    print(s)


xx = [n/10 for n in range(1,11)]
print(xx)


x = int(input("단을 입력하세요(2~9단) : "))


# # #
for i in range(1,10):
    print(x,"*",i,'=', x * i)
# # #


a = str(x) # a 추가! 혹은 x=input()으로 바로가기(=int()빼기!)

for i in range(1,10):
    print(x,"*",i,'=', a*i)

for i in range(2,10):
    print("구구단",i,'단 시작!', end =' ')
    for j in range(1,10):
        print(i*j,end=' ')
        print(' ')
