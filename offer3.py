#coding=utf-8

#在二维数组中查找某个值

array=[
    [1,2,8,9],
    [2,4,9,12],
    [4,7,10,13],
    [6,8,11,15]
]
print array[0][2]
def find(arr,num):
    '''
    
    :param arr: 
    :param num: 
    :return: boolean
    '''
    #代表行数
    row=0
    #代表列数
    col=len(arr[0])-1
    try:
        while(arr[row][col]):
            if(arr[row][col]==num):
                return True
            elif arr[row][col]>num:
                col-=1
            else:
                row+=1
    except:
        return False
print find(array,0)
