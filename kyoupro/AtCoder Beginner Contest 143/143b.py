n = int(input())
l = list(map(int, input().split()))
k = 0
for i in range(n):
    for a in range(i+1,n):
        k=k+l[i]*l[a]
print(k)
