# given N and M, print the sum of their last digits
# e.g. 13 12 -----> 3 + 2 = 5 ;  10 15 -----> 0 + 5 = 5

n, m = map(int, input().split())

print(n % 10 + m % 10)
