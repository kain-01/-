n,k =map(int,input().split())
l = list(map(int,input().split()))
c=0
for a in range(n):
    if l[a] >= k:
        c += 1
print(c)
