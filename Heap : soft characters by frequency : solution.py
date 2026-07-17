# Promblem - soft characters by frequency 
# Approach - max heap 
# Time and space complexity - 0(n) & 0(n) 
# Leetcode and diffculty level - 451 & medium 
class Solution {
public:
    string frequencySort(string s) {
        
        unordered_map<char,int> mp;

        for(char ch : s) {
            mp[ch]++;
        }

        priority_queue<pair<int,char>> pq;

        for(auto it : mp) {
            pq.push({it.second,it.first});
        }

        string ans = "";

        while(!pq.empty()) {

            int freq = pq.top().first;
            char ch = pq.top().second;

            pq.pop();

            while(freq--) {
                ans += ch;
            }
        }
        return ans;
    }
};
