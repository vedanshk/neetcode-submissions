class BrowserHistory {
    std::vector<string> history;
    int current_index;
    int last_index;

   public:
    BrowserHistory(string homepage) {
        history.push_back(homepage);
        current_index = 0;
        last_index = 0;
    }

    void visit(string url) {
         current_index++;
         if(current_index < history.size()){
            history[current_index] = url;
         }else{
            history.push_back(url);
         }
        
        last_index = current_index;
    }

    string back(int steps) {
        current_index = std::max(0, current_index - steps);
        return history[current_index];
    }

    string forward(int steps) {
        current_index = std::min(last_index, current_index + steps);
        return history[current_index];
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */