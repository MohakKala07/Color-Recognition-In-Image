#include<iostream>
#include<algorithm>

using namespace std;

struct color
{
    char name[25];
    long int code;
};

bool rules(color a, color b)
{ 
    return (a.code < b.code); 
} 

int main()
{
    int n;
    cout<<"Enter total colours:";
    cin>>n;
    color c[n];
    for(int i=0;i<n;i++)
        cin>>c[i].name>>c[i].code;

    sort(c, c+n, rules);

    cout<<"\n\n\n\nSORTED ARE FROM HERE:\n";
    for(int i=0;i<n;i++)
        cout<<c[i].name<<" "<<c[i].code<<endl;
    return 0;
}
