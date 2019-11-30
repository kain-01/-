n = int(input())
flag = 0
for a in range(1,10):
    for b in range(1,10):
        if a*b == n:
            flag += 1

if flag >= 1:
    print("Yes")
else:
    print("No")
