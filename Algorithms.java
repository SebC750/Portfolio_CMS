import java.util.ArrayList;

class Algorithm {
    private ArrayList<Integer> arr;

    public Algorithm(ArrayList<Integer> numberArray) {
        this.arr = numberArray;
    }

    public ArrayList<Integer> getArray() {
        return this.arr;
    }

    public void setArray(ArrayList<Integer> newArr) {
        this.arr = newArr;
    }

    public ArrayList<Integer> bubbleSort() {

        for (int i = 0; i < this.arr.size() - 1; i++) {
            boolean isSwapped = false;
            for (int j = 0; j < this.arr.size() - i - 1; j++) {
                int currentVal = this.arr.get(j);
                int nextVal = this.arr.get(j + 1);
                if (currentVal > nextVal) {
                    int temp = currentVal;
                    this.arr.set(j, nextVal);
                    this.arr.set(j + 1, temp);
                    isSwapped = true;
                }
            }
            if (!isSwapped) {
                return this.arr;
            }
        }
        return this.arr;
    }

    public ArrayList<Integer> selectionSort() {
        for (int i = 0; i < this.arr.size() - 1; i++) {
            int min = i;
            for (int j = i + 1; j < this.arr.size(); j++) {
                if (this.arr.get(min) > this.arr.get(j)) {
                    min = j;
                }
            }
            int temp = this.arr.get(i);
            this.arr.set(i, this.arr.get(min));
            this.arr.set(min, temp);
        }
        return this.arr;
    }

    public ArrayList<Integer> insertionSort() {
        for (int i = 1; i < this.arr.size(); i++) {
            int k = i - 1;
            while (k >= 0 && this.arr.get(i) < this.arr.get(k)) {
                int temp = this.arr.get(i);
                this.arr.set(i, this.arr.get(k));
                this.arr.set(k, temp);
                k -= 1;
            }
        }
        return this.arr;
    }
}
