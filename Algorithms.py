class Algorithms():
    def __init__(self, arr):
        self.array = arr
    def get_array(self):
        return self.array
    def set_array(self, new_arr):
        self.array = new_arr
    def bubble_sort(self):
        for i in range(0, len(self.array)):
            isSwapped = False
            for j in range(0, len(self.array) - i -1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    isSwapped = True
            
            if isSwapped == False:
                return self.array
        return self.array
    def selection_sort(self):
        for i in range(0, len(self.array)-1):
            min_idx = i
            for j in range(i, len(self.array)):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
        return self.array
    