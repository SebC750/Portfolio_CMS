import java.util.ArrayList;
class Algorithm {
    private ArrayList<Integer> arr;
    public Algorithm(ArrayList<Integer> numberArray){
            this.arr = numberArray;
    }
    public ArrayList<Integer> getArray(){
        return this.arr;
    } 
    public void setArray(ArrayList<Integer> newArr){
        this.arr = newArr;
    }
    public ArrayList<Integer> bubbleSort(){
        
        for(int i = 0; i < this.arr.size()-1; i++){
            boolean isSwapped = false;
            for(int j = 0; j < this.arr.size()-i-1; j++){
                 int currentVal = this.arr.get(j);
                 int nextVal = this.arr.get(j+1);
                 if(currentVal > nextVal){
                       int temp = currentVal;
                       this.arr.set(j, nextVal);
                       this.arr.set(j+1, temp);
                       isSwapped = true;
                 }
            }
            if(!isSwapped){
                return this.arr;
            }
        }
        return this.arr;
    }
}
