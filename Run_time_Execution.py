import time
import random
from demos import quick_sort,merge_sort,bubble_sort,selection_sort,insertion_sort

#Generate lists of random integers
n = int(input("Enter the number of elements:"))
n1 = int(input("Enter the range of integers:"))
n2 = int(input("Enter the number of runs:"))
List=[]
for i in range(n):
    List.append(random.randint(0,n1))


    
def analyse_func(func_name,arr):
    start = time.time()
    func_name(arr)
    stop = time.time()
    seconds = stop-start
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed time:{seconds:.5f}")
    
for i in range(n2):
    print(f"Run:{i+1}")
    analyse_func(quick_sort,List)
    analyse_func(merge_sort,List)
    #print(List)
    analyse_func(bubble_sort, List.copy())
    #print(List)
    analyse_func(selection_sort,List.copy())
    analyse_func(insertion_sort,List.copy())
    analyse_func(sorted,List)
    print("-"*40)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    