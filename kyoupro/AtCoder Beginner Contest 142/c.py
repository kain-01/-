N = int(input())
A = [int(i) for i in input().split()]
#2,3,1
ret = [0] * N   #0,0,0
for i in range(N):
    ret[A[i] - 1] = str(i + 1)   #if 2,0 = str(3)
print(" ".join(ret))