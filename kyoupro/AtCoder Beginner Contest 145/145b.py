n = int(input())
m = list(str(input()))
n1 = n//2
if n % 2 == 1:
    print("No")
else:
    if m[:n1] == m[n1:]:
        print("Yes")
    else:
        print("No")
