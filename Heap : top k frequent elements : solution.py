# promblem - top k frequent elements 
# Approach - min heap 
# Time and space complexity - 0(N log K ) & 0(n) 
# Leetcode and diffculty level - 347 & medium 
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mp;

        for(int num : nums) {
            mp[num]++;
        }

        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

        for(auto it : mp) {
            pq.push({it.second, it.first});

            if(pq.size() > k) {
                pq.pop();
            }
        }
        vector<int> ans;

        while(!pq.empty()) {
            ans.push_back(pq.top().second);
            pq.pop();
        }
        return ans;
    }
};
