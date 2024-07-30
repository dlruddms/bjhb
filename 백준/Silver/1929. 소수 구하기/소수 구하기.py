a, b = map(int,input().split())

for i in range(a,b+1):
    if i==1: #1은 소수 아님
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0: #약수가 존재해서 소수 아님
            break
    else:
        print(i)