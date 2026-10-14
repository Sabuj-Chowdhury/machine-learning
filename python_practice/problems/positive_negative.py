# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/C

count = int(input())

nums = list(map(int, input().split()))

even = 0
odd = 0
positive = 0
negative = 0


for i in  range(len(nums)) :
    if(nums[i] >0):
        positive +=1
    elif nums[i]<0 :
        negative +=1
    if nums[i] % 2 == 0 :
        even +=1
    else:
        odd +=1

print(f"Even: {even}\nOdd: {odd}\nPositive: {positive}\nNegative: {negative}")