#ifdef DEBUG
	#include "/Users/dimazhylko/CPPProjects/bits/stdc++.h"
#else
	#include <bits/stdc++.h>
#endif 

using namespace std;
//typedef long long ll;
//typedef long double ld;

#define f first
#define s second

struct pairhash {
public:
  template <typename T, typename U>
  std::size_t operator()(const std::pair<T, U> &x) const
  {
    return std::hash<T>()(x.first)*13 + std::hash<U>()(x.second)*7;
  }
};

bool ldfs(int v, vector<bool> &Vis, vector<int> &M, vector< vector<int> > &G, int n, int c, 
	unordered_map< pair<int, int>, pair<int, int>, pairhash > &costs){
	if(Vis[v])return false;
	Vis[v] = true;

	for(int u : G[v]){
		if(costs[{v, u-n}].f > c || costs[{v, u-n}].s < c)continue;

		if(M[u] == -1 || ldfs(M[u], Vis, M, G, n, c, costs)){
			M[u] = v;
			M[v] = u;
			return true;
		}
	}

	return false;
}

void turbo(int n, vector< vector<int> > &G, int c, unordered_map< pair<int, int>, pair<int, int>, pairhash > &costs,
	vector<int> &M){
	//fill(M.begin(), M.end(), -1);
	for(int i = 0;i<2*n;i++)M[i] = -1;
	vector<bool> Vis(n);

	bool incr = true;

	while(incr){
		incr = false;

		for(int u=0;u<n;u++)Vis[u]=false;
		for(int u = 0;u<n;u++){
			if(M[u]==-1 && ldfs(u, Vis, M, G, n, c, costs))incr = true;
		}
	}
}

int main(){
	ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
	
	int k;
	cin>>k;

	for(int t=0;t<k;t++){
		int n, m;
		cin>>n>>m;

		unordered_map< pair<int, int>, pair<int, int>, pairhash > costs(m);

		vector< vector<int> > G(n);

		int ll = 100000000;
		int rr = -1;

		for(int i = 0;i<m;i++){
			int from, to, l, u;
			cin>>from>>to>>l>>u;
			from--;to--;
			G[from].push_back(to+n);
			costs[{from, to}] = {l, u};
			ll = min(ll, l);
			rr = max(rr, l);
		}

		vector<int> M(2*n, -1);

		int res = -1;
		for(int i = ll;i<=rr;i++){
			turbo(n, G, i, costs, M);

			int c = 0;
			for(int j=0;j<n;j++)
				if(M[j] != -1)c++;
			if(c == n){
				res = i;
				break;
			}
		}

		if(res!=-1){
			cout<<res<<endl;
			for(int j = 0;j<n;j++){
				cout<<j+1<<" "<<M[j]-n+1<<endl;
			}
		} else {
			cout<<-1<<endl;
		}
	}

	return 0;
}