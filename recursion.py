import random
import time
#FUNCTION FOR USING MERGE SORT------------
def mergeSort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              numbers[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                numbers[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers[k]=right[j]
            j += 1
            k += 1
#FUNCTION FOR USING QUICK SORT------------
def partition (array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1
def quicksort(array,low,high):
    if low<high:
      pi=partition(array,low,high)
      quicksort(array,low,pi-1)
      quicksort(array,pi+1,high)

#FUNCTION FOR USING BUBBLE SORT --------------

def bubble_sort(numbers):  
      
    for i in range(0,len(numbers)-1):  
        for j in range(len(numbers)-1):  
            if(numbers[j]>numbers[j+1]):  
                temp = numbers[j]  
                numbers[j] = numbers[j+1]  
                numbers[j+1] = temp  
    return numbers
#FUNCTION FOR USING INSERTION SORT -------
def insertion_sort(numbers):
  
    # Traverse through 1 to len(numbers)
    for i in range(1, len(numbers)):
  
        key = numbers[i]
  
        
        j = i-1
        while j >=0 and key < numbers[j] :
                numbers[j+1] = numbers[j]
                j -= 1
        numbers[j+1] = key
#----------CODE FOR TAKING VALUES--------
n=int(input("How many random numbers you want ? : "))
start_value=int(input("Enter the starting range : "))
end_value=int(input("Enter the ending range : "))

start=time.time()
numbers=[]
for i in range(n):
     num=((random.randint(start_value,end_value)))
     numbers.append(num)
print("List of random numbers is : ",numbers)
#print("Unsorted data is : ",numbers)
# size=len(numbers)
# bubble_sort(numbers)
# print("Sorted data is -- " ,numbers)
# end=time.time()
# executiontime=(end)-(start)
# print("Execution time for BUBBLE SORT is : ",executiontime)
# size=len(numbers)
# mergeSort(numbers)
# # print("Sorted data using INSERTION SORT  is -- " ,numbers)
# end=time.time()
# executiontime=(end)-(start)
# print("Execution time for MERGE SORT is : ",executiontime)
insertion_sort(numbers)
# print("Sorted data using INSERTION SORT  is -- " ,numbers)
end=time.time()
executiontime=(end)-(start)
print("Execution time for Insertion Sort is : ",executiontime)
# quicksort(array, low, high)
# # print("Sorted data using INSERTION SORT  is -- " ,numbers)
# end=time.time()
# executiontime=(end)-(start)
# print("Execution time for QUICK SORT is : ",executiontime)