# Promblem - kth largest element in an array 
# Approach - min heap 
# Time and space complexity - 0( N log K ) & 0(k) 
# Leetcode and diffculty level - 215 & medium 
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> pq;

        for(int num : nums) {
            pq.push(num);

            if(pq.size() > k) {
                pq.pop();

            }
        }
        return pq.top();
    }
};
