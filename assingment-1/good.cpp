#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    int n;cin>>n;
    

    map<ll,ll>mp;
    for(int i=0;i<n;i++)
    {
        int c;cin>>c;
        mp[c]++;
    }

    int sum=0;
    for(auto it:mp)
    {
        if(it.second<it.first)
        {
            sum+=it.second;
        }
        else if(it.second>it.first)
        {
            sum+=it.second - it.first;
        }
    }
    
    cout<<sum<<endl;
}