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
    size_t h = (size_t(x.first)<<32)+size_t(x.second);
  	h*=1231231557ull; // "random" uneven integer
  	h^=(h>>32);
  	return h;
  }
};

bool ldfs(int v, vector<bool> &Vis, vector<int> &M, vector< vector<int> > &G, int n, int c, 
	unordered_map< pair<int, int>, pair<int, int>, pairhash > &costs){
	if(Vis[v])return false;
	Vis[v] = true;

	for(int u : G[v]){
		pair<int, int> co = costs[{v, u-n}];
		if(co.f > c || co.s < c)continue;

		if(M[u] == -1 || ldfs(M[u], Vis, M, G, n, c, costs)){
			M[u] = v;
			M[v] = u;
			return true;
		}
	}

	return false;
}

void turbo(int n, vector< vector<int> > &G, int c, unordered_map< pair<int, int>, pair<int, int>, pairhash > &costs,
	vector<int> &M, vector<bool> &Vis){
	fill(M.begin(), M.end(), -1);
	//for(int i = 0;i<2*n;i++)M[i] = -1;
	//vector<bool> Vis(n);

	bool incr = true;

	while(incr){
		incr = false;

		for(int u=0;u<n;u++)Vis[u]=false;
		for(int u = 0;u<n;u++){
			if(M[u]==-1 && ldfs(u, Vis, M, G, n, c, costs))incr = true;
		}
	}
}

bool is_isolated(int c, int n, vector< vector<int> > &G, unordered_map< pair<int, int>, pair<int, int>, pairhash > &costs){
	bool f = true;
	for(int i = 0;i<n;i++){
		for(int v : G[i]){
			pair<int, int> co = costs[{i, v-n}];
			if(co.f <= c && co.s >= c){
				f = false;
				break;
			}
		}
		if(f)return true;
		else f = true;
	}

	return false;
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

		unordered_map< pair<int, int>, pair<int, int>, pairhash > costs;
		costs.reserve(2*m);

		vector< vector<int> > G(n);

		vector<int> s(m);

		for(int i = 0;i<m;i++){
			int from, to, l, u;
			cin>>from>>to>>l>>u;
			from--;to--;
			G[from].push_back(to+n);
			costs[{from, to}] = {l, u};
			s[i] = l;
		}

		sort(s.begin(), s.end());
		int last = unique(s.begin(), s.end()) - s.begin();
		vector<int> M(2*n, -1);
		vector<bool> Vis(n);

		int res = -1;
		int c = 0;

		for(int i = 0;i<last;i++){
			//turbo(n, G, s[ll * ((i+1) % 2) + rr * (i % 2)], costs, M, Vis);

			if(is_isolated(s[i], n, G, costs))continue; // stolen from Agnieszka :* 

			turbo(n, G, s[i], costs, M, Vis);
			c = 0;
			for(int j=0;j<n;j++)
				c += M[j] != -1;
			if(c == n){
				res = s[i];
				break;
			}

			//ll += (i+1) % 2;
			//rr -= i%2;
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