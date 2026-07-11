# Promblem - remove stones to minimize the total 
# Approach - max heap
# Time and space complexity - 0(N + k(log N)) & 0(N) 
# Leetcode and diffculty level - 1962 & easy
class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        
        priority_queue<int> pq;

        for(int pile : piles) {
            pq.push(pile);
        }

        while(k--) {

            int largest = pq.top();
            pq.pop();

            largest = largest - largest / 2;
            pq.push(largest);
        }

        int sum = 0;

        while(!pq.empty()) {
            sum += pq.top();
            pq.pop();
        }
        return sum;
    }
};
