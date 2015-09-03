#include <assert.h>
#include <iostream>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        return this->isMatch(s, p, 0, 0);
    }
    
    bool isMatch(string s, string p, int si, int pi) {
        if (pi >= p.length()) return si == s.length();

        // next char is not '*': must match current character
        if (pi + 1 >= p.length() || p[pi + 1] != '*') {
            return ((p[pi] == s[si] || p[pi] == '.') && this->isMatch(s, p, si+1, pi+1));
        }
        
        // next char is '*'
        while (si < s.length() && (p[pi] == s[si] || p[pi] == '.')) {
            if (this->isMatch(s, p, si, pi+2)) return true;
            si++;
        }
        return this->isMatch(s, p, si, pi+2);
    }
};

int main( void )
{
    Solution *s = new Solution();
    cout<<(s->isMatch("aa", "a*") == true)<<endl;
    cout<<(s->isMatch("aa","a") == false)<<endl;
    cout<<(s->isMatch("aa","aa") == true)<<endl;
    cout<<(s->isMatch("aaa","aa") == false)<<endl;
    cout<<(s->isMatch("aa", "a*") == true)<<endl;
    cout<<(s->isMatch("aa", ".*") == true)<<endl;
    cout<<(s->isMatch("ab", ".*") == true)<<endl;
    cout<<(s->isMatch("aab", "c*a*b") == true)<<endl;
    cout<<(s->isMatch("a", "ab*") == true)<<endl;
    
}