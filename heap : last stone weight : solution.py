# Promblem - last stone weight 
# time and space complexity - 0(n log k) & 0(k) 
# Leetcode and diffculty level - 1046 & easy 
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {

        priority_queue<int> pq;

        for(int stone : stones) {
            pq.push(stone);
        }

        while(pq.size() > 1) {
            int first = pq.top();
            pq.pop();

            int second = pq.top();
            pq.pop();

            if(first != second) {
                pq.push(first - second);
            }
        }

        if(pq.empty()) {
            return 0;
        }
        return pq.top();
    }
};
