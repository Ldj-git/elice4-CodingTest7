#include <iostream>
#include <vector>
using namespace std;

// 금 줍기 / 하 / 15분풀고 한개 안되서 답지봄..

int main() {
    int n; cin >> n;
    int ret = 0;
    vector<int>gold;
    for (int i = 0; i < n; i++) {
        int tmp; cin >> tmp;
        gold.push_back(tmp);
    }
    int sum;
    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 3; j < n - 2; j++) {
            sum = 0;
            sum += gold[i] + gold[i + 1] + gold[i + 2];
            sum += gold[j] + gold[j + 1] + gold[j + 2];
            if (ret < sum) {
                ret = sum;
            }
        }
    }
    cout << ret;

    //엣지 케이스가 있는듯 그냥 한손으로 잡을때 최대치인곳 뽑고 배열에서 제거하고 한번더 했는데 이러면 탐지 안되는 경우가 있나봄
    //2n으로 할라했는데
    //그냥 n^2으로 해야되는듯
    /*vector<int>hanson;
    int maxloc = 0;
    for (int i = 0; i < gold.size() - 2; i++) {
        hanson.push_back(gold[i] + gold[i + 1] + gold[i + 2]);
        if (hanson[maxloc] < hanson[i]) {
            maxloc = i;
        }
    }


    ret += hanson[maxloc];
    gold.erase(gold.begin() + maxloc);
    gold.erase(gold.begin() + maxloc);
    gold.erase(gold.begin() + maxloc);


    hanson.clear();
    maxloc = 0;
    for (int i = 0; i < gold.size() - 2; i++) {
        hanson.push_back(gold[i] + gold[i + 1] + gold[i + 2]);
        if (hanson[maxloc] < hanson[i]) {
            maxloc = i;
        }
    }
    ret += hanson[maxloc];

    cout << ret;*/
}