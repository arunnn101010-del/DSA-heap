# Promblem - kth largest element in a stream 
# Time and space complexity - 0(N og k) & 0(k)
# Leetcode and diffulty level - 703 & easy 
class KthLargest {
public:
    priority_queue<int , vector<int>, greater<int>> pq;
    int k;

    KthLargest(int k, vector<int>& nums) {
        this->k = k;

        for(int num : nums) {
            pq.push(num);

            if(pq.size() > k ) {
                pq.pop();
            }
        }    
    }
    
    int add(int val) {
        pq.push(val);
        
        if(pq.size() > k) {
            pq.pop();
        }
        return pq.top();
    }
};
