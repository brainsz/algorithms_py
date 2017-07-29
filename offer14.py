#coding=utf-8

'''
调整数组的顺序使得奇数位于偶数前面
'''

def odd_even(arr,func):
    if arr==None or len(arr)==1:
        return arr
    left=0
    right=len(arr)-1
    while left<right:
        while left<right and not func(arr[left]):
            left+=1
        while left<right and func(arr[right]):
            right-=1
        if left<right:
            tmp=arr[left]
            arr[left]=arr[right]
            arr[right]=tmp
    return arr
def isEven(n):
    return (n&1)==0

print odd_even([1,2,3,4,5,6,7,8,9],isEven)
