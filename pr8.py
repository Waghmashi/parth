import numpy as np

class DataAnalytics:
    def __init__(self, array=None):
        self._array = array
    
    def create_array(self, dim_type, shape, elements):
        if dim_type == 1:
            self._array = np.array(elements)
        elif dim_type == 2:
            rows, cols = shape
            self._array = np.array(elements).reshape(rows, cols)
        else:
            d1, d2, d3 = shape
            self._array = np.array(elements).reshape(d1, d2, d3)
    
    def get_slice(self, row_slice, col_slice):
        return self._array[row_slice, col_slice]
    
    def math_op(self, op, other):
        if op == 1: return self._array + other
        elif op == 2: return self._array - other
        elif op == 3: return self._array * other
        elif op == 4: return self._array / other
        else: return np.dot(self._array, other)
    
    def combine(self, other, axis=0):
        return np.vstack([self._array, other]) if axis==0 else np.hstack([self._array, other])
    
    def search(self, val):
        return np.where(self._array == val)
    
    def sort_arr(self):
        return np.sort(self._array, axis=1)
    
    def aggregate(self, op):
        if op == 1: return np.sum(self._array)
        elif op == 2: return np.mean(self._array)
        elif op == 3: return np.median(self._array)
        elif op == 4: return np.std(self._array)
        else: return np.var(self._array)

class NumPyAnalyzer:
    def __init__(self):
        self.da = None
    
    def show_menu(self):
        print("\nChoose an option:\n1. Create a Numpy Array\n2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays\n4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics\n6. Exit")
    
    def create_array(self):
        print("\nSelect the type of array to create:\n1. 1D Array\n2. 2D Array\n3. 3D Array")
        ch = int(input("Enter your choice: "))
        
        if ch == 2:
            r = int(input("Enter the number of rows: "))
            c = int(input("Enter the number of columns: "))
            print(f"Enter {r*c} elements for the array separated by space: ", end="")
            elems = list(map(int, input().split()))
            self.da = DataAnalytics()
            self.da.create_array(2, (r, c), elems)
            print(f"Array created successfully: {self.da._array}")
            
            print("\n1. Indexing\n2. Slicing\n3. Go Back")
            sub = int(input("Enter your choice: "))
            if sub == 2:
                rs = input("Enter the row range (start:end): ").split(":")
                cs = input("Enter the column range (start:end): ").split(":")
                slice_r = slice(int(rs[0]), int(rs[1]))
                slice_c = slice(int(cs[0]), int(cs[1]))
                print(f"Sliced Array: {self.da.get_slice(slice_r, slice_c)}")
    
    def math_ops(self):
        if self.da is None:
            print("Create array first!")
            return
        
        print("\nChoose a mathematical operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        ch = int(input("Enter your choice: "))
        print(f"Original Array:\n{self.da._array}")
        
        elems = list(map(int, input("Enter the same-size array elements separated by space: ").split()))
        other = np.array(elems).reshape(self.da._array.shape)
        print(f"Second Array:\n{other}")
        
        res = self.da.math_op(ch, other)
        print(f"Result:\n{res}")
    
    def combine_split(self):
        if self.da is None:
            print("Create array first!")
            return
        
        print("\nChoose an option:\n1. Combine Arrays\n2. Split Array")
        ch = int(input("Enter your choice: "))
        
        if ch == 1:
            print("Enter the elements of another array to combine separated by space: ", end="")
            elems = list(map(int, input().split()))
            other = np.array(elems).reshape(self.da._array.shape)
            print(f"Original Array:\n{self.da._array}")
            print(f"Second Array:\n{other}")
            res = self.da.combine(other, 0)
            print(f"Combined Array (Vertical Stack):\n{res}")
        
        elif ch == 2:
            print("Enter the elements to create a new array for splitting (6 elements separated by space): ", end="")
            elems = list(map(int, input().split()))
            
            new_array = np.array(elems).reshape(2, 3)
            print(f"New Array created for splitting:\n{new_array}")
            
            split_parts = np.array_split(new_array, 2, axis=0)
            
            print(f"\nSplit array into 2 parts:")
            for i, part in enumerate(split_parts):
                print(f"Part {i+1}:\n{part}")
    
    def search_sort_filter(self):
        if self.da is None:
            print("Create array first!")
            return
        
        print("\nChoose an option:\n1. Search a value\n2. Sort the array\n3. Filter values")
        ch = int(input("Enter your choice: "))
        
        if ch == 2:
            print(f"Original Array:\n{self.da._array}")
            res = self.da.sort_arr()
            print(f"Sorted Array:\n{res} (Sorting applied row-wise.)")
    
    def aggregates_stats(self):
        if self.da is None:
            print("Create array first!")
            return
        
        print("\nChoose an aggregate/statistical operation:\n1. Sum\n2. Mean\n3. Median\n4. Standard Deviation\n5. Variance")
        ch = int(input("Enter your choice: "))
        print(f"Original Array:\n{self.da._array}")
        
        res = self.da.aggregate(ch)
        if ch == 1: print(f"Sum of Array: {res}")
        elif ch == 2: print(f"Mean of Array: {res}")
        elif ch == 3: print(f"Median of Array: {res}")
        elif ch == 4: print(f"Standard Deviation of Array: {res}")
        else: print(f"Variance of Array: {res}")
    
    def run(self):
        print("Welcome to the NumPy Analyzer!")
        
        while True:
            self.show_menu()
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                self.create_array()
            elif choice == 2:
                self.math_ops()
            elif choice == 3:
                self.combine_split()
            elif choice == 4:
                self.search_sort_filter()
            elif choice == 5:
                self.aggregates_stats()
            elif choice == 6:
                print("\nThank you for using the NumPy Analyzer! Goodbye!")
                break
            else:
                print("Invalid ch1oice!")

if __name__ == "__main__":
    analyzer = NumPyAnalyzer()
    analyzer.run()