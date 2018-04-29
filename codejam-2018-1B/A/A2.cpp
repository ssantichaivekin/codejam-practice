#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

const int INF = 1e9;
const int MAXN = 505;

int N,L;
int C[MAXN];
int need[MAXN];
int possible[MAXN];

typedef pair<int,int> ii;

int pass[MAXN][MAXN];
int dp[MAXN][MAXN];
int f(int n, int r){
  if(n == N+L+1){
    if(r > 0) return -INF;
    return 0;
  }

  if(pass[n][r]) return dp[n][r];
  pass[n][r] = true;

  int maxval = 0;
  int ratio;
  if(n <= L){
    for(int i=0;i<=r;i++){
      ratio = (100*(C[n] + i) + N/2) / N;
      maxval = max(maxval, ratio + f(n+1, r-i));
    }
  }else{
    for(int i=1;i<=r;i++){
      ratio = (100*i + N/2) / N;
      maxval = max(maxval, ratio + f(n+1, r-i));
    }
  }
  return dp[n][r] = maxval;
}

int run(){
  scanf("%d %d", &N, &L);
  memset(C, 0, sizeof C);
  memset(possible, 0, sizeof possible);
  memset(need, 0, sizeof need);
  memset(pass, 0, sizeof pass);
  memset(dp, 0, sizeof dp);

  int remains = N;
  for(int i=1;i<=L;i++){
    scanf("%d",&C[i]);
    remains -= C[i];
  }

  return f(1,remains);
}

int main(){
  int T;
  scanf("%d", &T);
  for(int i=1;i<=T;i++){
    printf("Case #%d: %d\n", i, run());
  }
  return 0;
}