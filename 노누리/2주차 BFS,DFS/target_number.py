def solution(numbers, target):
    cnt=0
    
    def recur(idx,sum_num):
        nonlocal cnt
        if idx==len(numbers):
            if sum_num==target:
                cnt+=1
            return
        recur(idx+1,sum_num+numbers[idx])
        recur(idx+1,sum_num-numbers[idx])
    
    recur(0,0)
    
    return cnt
