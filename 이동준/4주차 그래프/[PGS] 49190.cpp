#include <string>
#include <vector>
#include <string.h>
#include <iostream>
#include <set>

using namespace std;

// [PGS] 49190. 방의 개수 / 레벨 5 / 2시간 이상

int solution(vector<int> arrows) {
    int answer = 0;

    //그래프로 어캐 바꾸지
    //아 그냥 에로우 따라가면서 이미 방문한 점인지 아닌지만 확인?
    //안될거 같긴한데 dfs하면서 방문한곳 재방문 하면 도형 그려진걸로 인식?

//     vector<bool>tmp(100000,false);
//     vector<vector<bool>>visited(100000,tmp);
//     int x = 50000, y = 50000;
//     int dirx[8] = { 0,1,1,1,0,-1,-1,-1 };
//     int diry[8] = { 1,1,0,-1,-1,-1,0,1 };
//     visited[x][y] = true;
//     for (int i = 0; i < arrows.size(); i++) {
//         x += dirx[arrows[i]];
//         y += diry[arrows[i]];
//         if (visited[x][y])
//             answer++;

//         visited[x][y] = true;
//     }
    //이 방법 문제가 이미 갔던곳 또가면 또세서 그거 탐지 해줘야댐
    
    //질문 하기 참고
    //https://ko.wikipedia.org/wiki/%EC%98%A4%EC%9D%BC%EB%9F%AC_%EB%8B%A4%EB%A9%B4%EC%B2%B4_%EC%A0%95%EB%A6%AC
    //오일러 뭐시기인데 면=1-선+점 이네
    //선갯수랑 점 갯수만 세면 되긴함
    
    set<pair<int,int>>vertex;
    set<pair<pair<int,int>,pair<int,int>>>edge;
    
    int dirx[8] = { 0,1,1,1,0,-1,-1,-1 };
    int diry[8] = { 1,1,0,-1,-1,-1,0,1 };
    int x=0,y=0;
    for (int i = 0; i < arrows.size(); i++) {
        int tmpx=x,tmpy=y;
        x += dirx[arrows[i]];
        y += diry[arrows[i]];
        vertex.insert(make_pair(x,y));
        edge.insert(make_pair(make_pair(x,y),make_pair(tmpx,tmpy)));
        edge.insert(make_pair(make_pair(tmpx,tmpy),make_pair(x,y)));
    }
    
    
    //대각선으로 교차할때 점이 하나 더생김...
    //모든 엣지 다 확인하면서 교차 하면 점으로 추가
    int xdot=0;
    for(auto iter=edge.begin();iter!=edge.end();iter++){
        pair<pair<int,int>,pair<int,int>> tmp=*iter;
        //1번모양 선인경우로 한정 헷갈려서..
        if(tmp.second.first-tmp.first.first==1&&tmp.second.second-tmp.first.second==1){
            //3번 모양 선 있는지 확인
            tmp.first.second+=1;
            tmp.second.second-=1;
            if(edge.find(tmp)!=edge.end()){//존재 하면 점 추가
                xdot++;
            }
        }     
    }
    
    cout<<vertex.size()<<" "<<xdot<<" "<<edge.size()/2;
    return 1-vertex.size()+xdot+edge.size()/2;
    //정확성 55.6뜨는데 뭔지 모르겠어서 포기
}