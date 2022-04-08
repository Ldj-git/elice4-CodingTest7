from collections import deque

def solution(begin, target, words):
    answer = 0
    queue=deque([[begin,0]])
    visited=[]
    
    while queue:
        node,dis=queue.popleft()
        if node==target:
            answer=dis
            break
        for i in range(len(words)):
            cnt=0
            if words[i] not in visited:
                for j in range(len(node)):
                    if node[j]!=words[i][j]:
                        cnt+=1
                if cnt==1:
                    queue.append([words[i],dis+1])
                    visited.append(words[i])

    return answer
