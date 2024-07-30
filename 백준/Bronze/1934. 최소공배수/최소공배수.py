import sys

input = sys.stdin.readline

def gcd(N, M):
    
    if(M == 0):
        return N
    
    return gcd(M, N%M)

T = int(input()) # 테스트 케이스의 개수

for _ in range(T):
    N, M = map(int, input().split()) # 최대 공약수랑 최소 공배수를 구할 값
    
    g = gcd(N, M)
    lcm = int((N*M) / g)
    
    print(lcm)
