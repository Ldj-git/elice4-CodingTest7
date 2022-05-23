def main():
    X = input()
    X = X.split(' ')
    # 세로길이 N, 가로길이 M, 당근 개수 K
    N = int(X[0])
    M = int(X[1])
    K = int(X[2])
    
    n = []
    m = []
    
    for i in range(K):
        k = input()
        k = k.split(' ')

        n.append(int(k[0]))
        m.append(int(k[1]))
    
    n.sort()
    m.sort()
    
    result = (n[-1] - n[0] + 2) * 2 + (m[-1] - m[0] + 2) * 2
    print(result)
    
if __name__=="__main__":
    main()