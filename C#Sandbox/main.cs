using System.Collections;
class helloWorld{
    static void Main(string[] args){
        Console.WriteLine("Hello world!");
        Console.WriteLine("This is my new program!");

        int number = 1;
        Console.WriteLine("Number: "+number);
        string arrayName = "Myarray";
        Console.WriteLine("New array name: "+arrayName);
        int count = 10;
        //Testing count
        while(count > 0){
            Console.WriteLine("Current countdown: "+count);
            count--;
        }
        //Testing for loop
        int sum = 0;
        for(int i = 0; i < 10; i++){
            sum += i;
            Console.WriteLine("Current sum: "+sum);
        }
        ArrayList nums = new ArrayList();
        nums.Add(2);
        nums.Add(5);
        nums.Add(1);
        nums.Add(3);
        nums.Add(6);
        nums.Add(8);
        nums.Add(7);
        nums.Add(10);
        nums.Add(9);
        
        for(Int32 i: nums){
            
        }
        
        //Bubble sort
        
    }
    
    
}