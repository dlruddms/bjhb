from collections import deque

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = int(input())
C= list(map(int,input().split()))

dq = deque([])

for i in range(n):
    if A[i] ==0: #큐인 자료구조만 생각하겠다
        dq.append(B[i])

for i in range(M):
    dq.appendleft(C[i])
    print(dq.pop(),end=' ')
