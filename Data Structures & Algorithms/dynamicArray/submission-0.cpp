class DynamicArray {
    int* arr;
    int capacity;
    int size;

   public:
    DynamicArray(int capacity) {
        this->capacity = capacity;
        arr = new int[capacity];
        size = 0;
    }

    int get(int i) {
        if (i >= 0 && i < capacity) {
            return arr[i];
        }

        return -1;
    }

    void set(int i, int n) {
        if (i >= 0 && i < capacity) {
            arr[i] = n;
        }
    }

    void pushback(int n) {
        if (size == capacity) {
            int newCapacity = 2 * capacity;
            int* newArr = new int[newCapacity];
            // now copy element from old to new
            for (int i = 0; i < size; ++i) {
                newArr[i] = arr[i];
            }
            delete[] arr;

            arr = newArr;
            capacity = newCapacity;
        }
        arr[size] = n;
        size++;
    }

    int popback() {
        if (size == 0) {
            return -1;  // or throw an exception
        }
        int lastEle = arr[size - 1];
        size--;
        return lastEle;
    }

    void resize() {
        int newCapacity = capacity * 2;
        int* newArr = new int[newCapacity];

        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }

        delete[] arr;
        arr = newArr;
        capacity = newCapacity;
    }

    int getSize() { return size; }

    int getCapacity() { return capacity; }

    ~DynamicArray(){
        delete[] arr;
    }
};
