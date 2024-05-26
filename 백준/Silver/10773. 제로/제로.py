K = int(input())
A = []
for _ in range(K):
  N = int(input())
  if N != 0:
    A.append(N)
  else:
    A.pop()
  
print(sum(A))