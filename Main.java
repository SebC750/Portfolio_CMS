import java.util.ArrayList;
class Main{
    public static void main(String[] args) {
        //System.out.println("Hello world!");
        ArrayList<Integer> numbers = new ArrayList<>();
        for(int i = 0; i < 10; i++){
            int randVal = (int) (Math.random() * 900) + 100;
            numbers.add(randVal);
        }

        Algorithm al1 = new Algorithm(numbers);
       /* 
        * ArrayList<Integer> result = al1.bubbleSort();
        for(Integer i: result){
            System.out.println(i);
        }
       */
        
        /* 
         * 
         * ArrayList<Integer> selectResult = al1.selectionSort();
        for(Integer i: selectResult){
            System.out.println(i);
        }
        */
        ArrayList<Integer> insertionResult = al1.insertionSort();
        for(Integer i: insertionResult){
            System.out.println(i);
        }


    }
}