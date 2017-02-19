# find product feb 19/2017

import sys
length=int(input())
num=list(map(int,input().split()))           #to convert the string of numbers into a single number
mul=1
for i in range(0,length):
    mul=(mul*num[i])%(1000000007)             # find the product
print (mul)
