class Solution {
   public:
    int calPoints(vector<string>& operations) {
        stack<int> st;

        for (string op : operations) {
            if (op == "+") {
                // record sum previous records
                int first = st.top();
                st.pop();
                int second = st.top();
                int third = first + second;
                st.push(first);
                st.push(third);
            } else if (op == "C") {
                // invalidate remove previous score
                st.pop();
            } else if (op == "D") {
                int first = st.top();
                st.push(first*2);

            } else {
                int num = std::stoi(op);
                st.push(num);
            }
        }
        int sum = 0;
        while (!st.empty()) {
            int temp = st.top();
            st.pop();
            sum += temp;
        }
        return sum;
    }
};