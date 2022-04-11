def solution(tickets):
    answer=[]
    stack=["ICN"]
    diction={}
    
    for i in range(len(tickets)):
        if tickets[i][0] in diction:
            diction[tickets[i][0]].append(tickets[i][1])
        else:
            diction[tickets[i][0]]=[tickets[i][1]]
            
    for key in diction.keys():
        diction[key].sort()
        
    while stack:
        n=stack[-1]
        if diction.get(n):
            stack.append(diction[n].pop(0))
        else:
            answer.append(stack.pop())
            
    return answer[::-1]
