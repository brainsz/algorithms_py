#coding=utf-8
"""
Given n processes, each process has a unique PID (process id) and its PPID (parent process id).

Each process only has one parent process, but may have one or more children processes. This is just like a tree structure. Only one process has PPID that is 0, which means this process has no parent process. All the PIDs will be distinct positive integers.

We use two list of integers to represent a list of processes, where the first list contains PID for each process and the second list contains the corresponding PPID.

Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that will be killed in the end. You should assume that when a process is killed, all its children processes will be killed. No order is required for the final answer.

Example 1:
Input: 
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
Output: [5,10]
Explanation: 
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10
"""
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        # d = collections.defaultdict(list)
        # 建立pid，ppid的对应表，如pid=[0,1,2,3,4,5],ppid=[0,1,1,1,1]
        # # 通过下面的代码得到map{0：[0],1:[2,3,4,5]}
        # for c, p in zip(pid, ppid): d[p].append(c)
        #
        # bfs = [kill]  # 最后的BFS结果中第一个元素是kill
        # for i in bfs: bfs.extend(d.get(i, []))  # 把结果的子进程添加进来
        # return bfs

        '''def get_keys(d, value):
            return [k for k, v in d.items() if v == value]
        d={}
        res=[]
        kill_list=[]
        kill_list.append(kill)
        for i in range(len(pid)):
            d[pid[i]]=ppid[i]
        while kill_list:
            elem=kill_list.pop()
            res.append(elem)
            remain=get_keys(d,elem)
            if not remain:
                continue
            for key in remain:
                kill_list.append(key)
        return res'''
        d = dict()
        #enumerate 是枚举 可以同时获得索引和它的值
        for i,v in enumerate(ppid):
            if v in d:
                d[v].append(pid[i])
            else:
                d[v]=[pid[i]]
        stack = [kill]
        ans =[]
        while len(stack) != 0:
            cur = stack.pop()
            if cur in d:
                stack += d[cur]
            ans.append(cur)
        return ans



ss=Solution()
print ss.killProcess(pid, ppid, kill)




