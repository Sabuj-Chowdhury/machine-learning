# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/K

a, b, c = map(int, input("enter 3 number to find the minimum and maximum: ").split())

if a >= b and a >= c:
    max_val = a
elif b >= a and b >= c:
    max_val = b
else:
    max_val = c

if a <= b and a <= c:
    min_val = a
elif b <= a and b <= c:
    min_val = b
else:
    min_val = c

print(f"{min_val} {max_val}")
