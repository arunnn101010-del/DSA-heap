# Promblem - take gift from the richest pile 
# Appraoch - max heap 
# Time and space complexity - 0(N + K(log N)) & 0(N) 
# Leetcode and diffculty level - 2558 & easy
class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        
        priority_queue<int> pq;

        for(int gift : gifts) {
            pq.push(gift);
        }

        while(k--) {
            int largest = pq.top();
            pq.pop();

            pq.push(sqrt(largest));
        }

        long long sum = 0;

        while(!pq.empty()) {

            sum += pq.top();
            pq.pop();
        }
        return sum;
    }
};
