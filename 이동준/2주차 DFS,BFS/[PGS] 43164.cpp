#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

//[PGS] 43164. 여행경로 / 레벨 3 / 45분

vector<vector<string>>possible; //가능한 모든 경로 저장용
//here는 현재 위치, used는 사용된 티켓 저장용, now는 현재까지 온 경로 저장용, 티켓은 문제 입력
void dfs(string here,vector<int>used, vector<string> now,vector<vector<string>> tickets){
    now.push_back(here);
    if(now.size()==used.size()+1){ //티켓 다 사용해서 종료
        possible.push_back(now);
        return;
    }
    for(int i=0;i<tickets.size();i++){
        if(tickets[i][0]==here&&used[i]==0){
            used[i]=1;
            dfs(tickets[i][1],used,now,tickets);
            used[i] = 0; //이거 빼먹어서 10분 날림
        }
    }
}

vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer;
    vector<int>used(tickets.size(),0);
    
    //처음에 bfs로 하다가 dfs로 바꿈
    //해당 시점의 티켓 사용여부를 다 다르게 봐줘야 돼서
    //그니까 모든 가능한 경우의 수를 다 찾아보는거
    dfs("ICN",used,{},tickets);
    
    sort(possible.begin(),possible.end()); //알파벳순 정렬
    answer=possible[0];
    return answer;
}

    // //처음에 짠 bfs 코드 (티켓을 알파벳순으로 정렬했었음)
    // queue<string>q;
    // q.push("ICN");
    // while(!q.empty()){
    //     string here=q.front(); q.pop();
    //     answer.push_back(here);
    //     for(int i=0;i<tickets.size();i++){
    //         if(tickets[i][0]==here&&used[i]==0){
    //             used[i]=1;
    //             q.push(tickets[i][1]);
    //             break;
    //         }
    //     }
    // }

    // 제대로 됐나 출력용
    // for(int i=0;i<possible.size();i++){
    //     for(int j=0;j<possible[i].size();j++){
    //         cout<<possible[i][j]<<" ";
    //     }
    //     cout<<"\n";
    // }