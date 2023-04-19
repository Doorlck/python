#논리연산자를 이용하지 않고
#3과 5의 공배수 처리하기
#3과 5의 최소공배수는 15

for i in range(1,101):
    if i % 15 ==0 :
        print('FizzBuzz')
    if i % 3 ==0 :
        print('fizz')
    elif i % 5 ==0 :
        print('buzz')
    else :
        print(i)

#논리연산자를 이용하여 
#3과 5의 공배수 처리하기
#3과 5의 공배수를 확인하는 코드를
#맨 앞에 써야 함. 안그러면 
#그대로 3의 배수인 것만 확인하고
#코드탈출 할 수 있음

for i in range(1,101):
    if i%3==0 and i%5==0 :
        print('fizzbuzz')
    elif i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else:
        print(i)



