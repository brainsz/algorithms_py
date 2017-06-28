#coding=utf-8

#求旋转数组最小值

def min_num(array):
    if (array is None) or len(array)==0:
        return None
    if len(array)==1:
        return array[0]
    p1=0
    p2=len(array)-1
    mid=p1
    while array[p1]>=array[p2]:
        if p2-p1==1:
          mid=p2
          break
        mid=(p1+p2)//2
        if (array[mid]>=array[p1]):
            p1=mid
        elif array[mid]<=array[p2]:
            p2=mid
    return array[mid]
print min_num([])