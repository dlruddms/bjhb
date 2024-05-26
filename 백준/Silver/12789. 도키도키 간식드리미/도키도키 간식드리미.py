import sys



n = int(input())
l = list(map(str,input().split()))
com_list = [str(x) for x in range(1,n+1)]
tmp_list = [' ']
ans_list = list()
cnt = 0

while len(ans_list) != n:
    if l[0] == com_list[cnt]:
        ans_list.append(l.pop(0))
        cnt +=1
    else:
        if tmp_list[-1] == com_list[cnt]:
            ans_list.append(tmp_list.pop())
            cnt+=1
        else:
            tmp_list.append(l.pop(0))
    if len(l)==0:
        while len(tmp_list) != 0:
            ans_list.append(tmp_list.pop())
        break
    
if ''.join(ans_list).rstrip() == ''.join(com_list):
    print('Nice')
else:
    print('Sad')
    