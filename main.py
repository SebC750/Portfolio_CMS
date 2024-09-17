import random
import Algorithms
from Algorithms import Algorithms

def main():
    
    array = [9,1,3,2,4,7,5,6,10,8]
    
    bubble_array = [x for x in array]
    print("Bubble sort array: "+str(bubble_array))
    bubble_algor = Algorithms(bubble_array)
    result = bubble_algor.bubble_sort()
    print(result)
  
    selection_array = [x for x in array]
    print("Selection sort array: "+str(selection_array))   
    select_algor = Algorithms(selection_array)
    print(select_algor.get_array())
    result2 = select_algor.selection_sort()
    print(result2)
    

main()