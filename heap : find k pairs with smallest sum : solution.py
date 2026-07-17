# Promblem - find k pairs with smallest sum 
# Approach - max heap 
# Time and space complexity - 0(m * n + log k ) & 0(k) 
# Leetcode and diffculty level - 373 & medium 
class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {

        vector<vector<int>> ans;

        if(nums1.empty() || nums2.empty() || k == 0)
            return ans;

        priority_queue<
            pair<int, pair<int,int>>,
            vector<pair<int, pair<int,int>>>,
            greater<pair<int, pair<int,int>>>
        > pq;

        for(int i = 0; i < min((int)nums1.size(), k); i++) {
            pq.push({nums1[i] + nums2[0], {i, 0}});
        }

        while(k-- && !pq.empty()) {

            auto top = pq.top();
            pq.pop();

            int i = top.second.first;
            int j = top.second.second;

            ans.push_back({nums1[i], nums2[j]});

            if(j + 1 < nums2.size()) {
                pq.push({nums1[i] + nums2[j + 1], {i, j + 1}});
            }
        }

        return ans;
    }
}
