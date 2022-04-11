#include <string>
#include <vector>
#include <iostream>

using namespace std;

//[PGS] 43162. 네트워크 / 레벨 3 / 15분

int visited [200];
int answer = 0;

//computers랑 n을 전역으로 받을수가 없어서 이렇게 넘겨줬읍니다
void dfs(int here,int n, vector<vector<int>> computers){ 
    if(visited[here]==0){ //처음 방문 확인
        visited[here]=answer; //방문 하면 해당 위치를 현재의 answer로 업데이트 했습니다. 디버깅하기 좋게 하려고
        for(int i=0;i<n;i++){
            if(computers[here][i]==1&&visited[i]==0){
                dfs(i,n,computers);
            }
        }
    }
}

int solution(int n, vector<vector<int>> computers) {    
    //dfs로 해보겠심미더
    for(int i=0;i<n;i++){
        //처음 방문하는 곳이니까 answer하나 올려주기
        if(visited[i]==0){
            answer++;
        }
        //dfs로 방문 가능한 (네트워크로 연결된) 모든 노드 방문하기
        dfs(i,n,computers);
    }
    
    return answer;
}