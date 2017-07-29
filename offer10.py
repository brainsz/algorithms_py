#coding=utf-8

'''
二进制中1的个数
把一个整数n和他减去1之后的数做与运算，会把最后一个1变为0
'''
def numerOf1(n):
    count=1
    while n:
        n=n&n-1
        count+=1
    return count
print numerOf1(23)