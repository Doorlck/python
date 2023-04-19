# 반복문 안에 반복문이 들어 있는 형태를
# 중첩 루프라고 하며 루프 인덱스 변수는
# i부터 순서대로 짓습니다.
# 예) i, j, k
# 중첩 루프는 주로 가로×세로 형태로 된
# 2차원 평면을 다룰 때 사용합니다

#사각형 만들기
# for i in range(5):
#     for j in range(5):
#         print('j:',j,sep='',end=' ')
#     print('i:',i,sep='')

#대각선으로 별 출력하기
for i in range(5):
    for j in range(5):
        if i==j :
            print('*',end='')
        else :
            print(' ',end='')
    print()        


