def solution(n, computers):
    answer = 0
    
    lst = [[] for i in range(n)]
    check = [0] * n
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                lst[i].append(j)
    

    networks = []
    
    for i in range(n):
        if check[i] == 1:
            continue
        network = []
        stack = [i]

        while stack:
            computer = stack.pop()
            if computer not in network:
                network.append(computer)
                stack += lst[computer]
                check[computer] = 1
            if network not in networks:
                networks.append(network)

    answer = len(networks)
    return answer