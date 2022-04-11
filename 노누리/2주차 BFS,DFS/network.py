def solution(n, computers):
    answer = 0
    stack=[0]*n
        
    def dfs(root):
        if stack[root]==1:
            return
        stack[root]=1
        for i in range(n):
            if computers[root][i]==1 and root!=i:
                dfs(i)
        
    for i in range(n):
        if stack[i]==0:
            dfs(i)
            answer+=1
        
    return answer
