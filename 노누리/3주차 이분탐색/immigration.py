def solution(n, times):
    answer = 0
    left=min(times)
    right=max(times)*n
    
    while left<=right:
        cnt=0
        mid=(left+right)//2
        for t in times:
            cnt+=mid//t
            
        if cnt<n:
            left=mid+1
        elif cnt>=n:
            right=mid-1
            answer=mid
            
    return answer
