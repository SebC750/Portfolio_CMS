import java.util.ArrayList;
class Main{
    public static void main(String[] args) {
        //System.out.println("Hello world!");
        ArrayList<Integer> numbers = new ArrayList<>();
        for(int i = 0; i < 1000; i++){
            int randVal = (int) (Math.random() * 900000) + 100000;
            numbers.add(randVal);
        }

        Algorithm al1 = new Algorithm(numbers);

        ArrayList<Integer> result = al1.bubbleSort();
        for(Integer i: result){
            System.out.println(i);
        }
    }
}