#4949
import sys
n = ''
while n != '.':
    result = [] #Yes,no를 판단하기위한 조건을 담아주는 리스트
    l=[] #()[] 만 담아주기위한 리스트
    n = sys.stdin.readline().rstrip() 
    if n =='.':
        break #.를 입력받을때 while 정지
    for i in n:
        if i in "()[]":
            l.append(i) #()[] 만 l에 저장
    for j in l:
        if j in "([":
            result.append(j) #(, [ 만 result에 저장
        else:
            if len(result)==0:
                result.append(1) #result == 0 을 기준으로 보기 때문에 조건에 안맞게 강제 수정 
                break
            else:
                if j ==')': 
                    if result[-1]=='(':
                        result.pop()
                    else:
                        break
                elif j == ']':
                    if result[-1]=='[':
                        result.pop()
                    else:
                        break
    if len(result)==0:
        print('yes')
    else:
        print('no')