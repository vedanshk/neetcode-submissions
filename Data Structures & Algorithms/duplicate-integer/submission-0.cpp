class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> um;
        for(int el:nums){
            if(um[el] == 1){
                return true;
            }else{
                um[el]++;
            }
        }
        return false;
    }
};