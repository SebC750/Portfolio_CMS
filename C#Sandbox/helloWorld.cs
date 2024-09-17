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

        //Bubble sort
        int[] nums = {2,4,1,9,7,5,6,10,8};
        int[] sortedNums = bubbleSort(nums);
        string showNums = "";
        for(int num = 0; num < sortedNums.Length-1; num++){
            showNums += sortedNums[num];
        }
        Console.WriteLine(showNums);
    }
    static int[] bubbleSort(int[] numArray){
        
        for(int i = 0; i < numArray.Length-1;i++){
            bool isSwapped = false;
            for(int j = 1; j < numArray.Length - i;j++){
                if( numArray[j] < numArray[j-1]){                  
                    int temp = numArray[j];
                    numArray[j] = numArray[j-1];
                    numArray[j-1] = temp;                   
                    isSwapped = true;
                }           
            }
            if(!isSwapped){
                return numArray;
            }     
        }
        return numArray;
    }
}