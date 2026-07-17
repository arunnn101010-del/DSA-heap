# Promblem - kth smallest element in a matrix 
# Approach - max heap 
# Time and space complexity - 0(n log k) & 0(n)
# Leetcode and diffculty level - 378 & medium 
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {

        priority_queue<int> pq;

        for(auto &row : matrix){

            for(int num : row){

                pq.push(num);

                if(pq.size() > k){
                    pq.pop();
                }
            }
        }

        return pq.top();
    }
};
