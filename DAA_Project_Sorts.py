import random
import time
import os
import tkinter as tk
from tkinter import messagebox

# =============================================================================
def merge(left,right):
     sorted_list=[] 
     i,j=0,0
     while i<len(left) and j<len(right):
         if left[i] < right[j]:
             sorted_list.append(left[i])
             i+=1
         else:
             sorted_list.append(right[j])
             j+=1
 
     sorted_list+=left[i:]
     sorted_list+=right[j:]
     return sorted_list
 
def merge_sort(li):
     if len(li)==1:
         return li
     middle=int(len(li)/2)
     left_li=merge_sort(li[:middle])
     right_li=merge_sort(li[middle:])
     return merge(left_li,right_li)
# =============================================================================

# =============================================================================
def insertion_sort(li):
     for i in range(1, len(li)):
         j = i
         while li[j] < li[j-1] and j > 0:
             li[j], li[j-1] = li[j-1], li[j]
             j -= 1
             
     return li
# =============================================================================


# =============================================================================
def selection_sort(li):
     for index in range(len(li) - 1, 0, -1):
         max_position = 0
         for location in range(1, index + 1):
             if li[location] > li[max_position]:
                 max_position = location
 
         li[index],li[max_position] = li[max_position],li[index]
 
     return li
# =============================================================================


# =============================================================================
# 
def bubble_sort(li):
    for no in range(len(li)-1, 0, -1):
        for i in range(no):
            if li[i] > li[i+1]:
                li[i],li[i+1] = li[i+1],li[i]

    return li
# =============================================================================



# =============================================================================
# 
def heap_sort(li):
    n = len(li)
    for i in range(n, -1, -1):
        max_heapify(li, i, n)

    n -= 1
    while n > 0:
        li[0], li[n] = li[n], li[0]
        max_heapify(li, 0, n)
        n -= 1
        
    return li


def max_heapify(arr, i, n):
    largest = i
    left_child = (i*2)+1
    right_child = (i*2)+2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, n)
# =============================================================================


# =============================================================================
# 
        
    
        
def quick_sort(li):
    def helper(arr, first, last):
        if first < last:
            split = partition(arr, first, last)

            helper(arr, first, split - 1)
            helper(arr, split + 1, last)


   
    def median(a, i, j, k):
          if a[i] < a[j]:
            return i if a[k] < a[i] else k if a[k] < a[j] else j
          else:
            return j if a[k] < a[j] else k if a[k] < a[i] else i
    
    def partition(arr, first, last):
        
        if input_algorithm == '6':
            pivot_value = arr[first]
        elif input_algorithm == '7':
            pivotindex = median(arr, first, last, int((first+last)/2))
            arr[first], arr[pivotindex] = arr[pivotindex], arr[first]
            pivot_value = arr[first]

        left = first+1
        right = last

        done = False
        while not done:
            while left <= right and arr[left] <= pivot_value:
                left += 1

            while arr[right] >= pivot_value and right >= left:
                right -= 1

            if right < left:
                done = True
            else:
                arr[left],arr[right] = arr[right],arr[left]

        arr[first],arr[right] = arr[right],arr[first]

        return right

    helper(li, 0, len(li) - 1)
    return li


# =============================================================================

# =============================================================================
def main_func(): 
    global input_algorithm
    global input_list_size
    global input_type
    global input_list
    
    input_algorithm=input1.get()
    input_list_size=input2.get()
    input_type=input3.get()
    input_list=[]
    
    if input_type=='1':
        input_type_string = 'Ascending'
        for i in range(0,int(input_list_size)):
            i += 1
            input_list.append(i)
    elif input_type=='2':
        input_type_string = 'Descending'
        for i in range(int(input_list_size),0,-1):
            i -= 1
            input_list.append(i)
    elif input_type=='3':    
        input_type_string = 'Random'
        for i in range(0,int(input_list_size)):
            n = random.randint(1,int(input_list_size)+1)
            input_list.append(n)
    else:
        print("Invalid input type selection.")
        return
    
    start = time.time()
    if input_algorithm=='1':
        algo = 'Merge Sort'
        output = merge_sort(input_list.copy())
    
    elif input_algorithm=='2':
        algo = 'Insertion Sort'
        output = insertion_sort(input_list.copy())
    
    elif input_algorithm=='3':
        algo = 'Selection Sort'
        output = selection_sort(input_list.copy())
    
    elif input_algorithm=='4':
        algo = 'Bubble Sort'
        output = bubble_sort(input_list.copy())
        
    elif input_algorithm=='5':
        algo = 'Heap Sort'
        output = heap_sort(input_list.copy())
    
    elif input_algorithm=='6':
        algo = 'Quick Sort(Regular)'
        output = quick_sort(input_list.copy())
        
    elif input_algorithm=='7':
        algo = 'Quick Sort(Median Of Three)'
        output = quick_sort(input_list.copy())
            
    else:
        print("Invalid algorithm selection.")
        return
    
    if 1 <= int(input_algorithm) <= 7:
            
        end = time.time()
        proc_time = (end - start)
        
        messagebox.showinfo("Success",f"Algorithm: {algo}\nInput: {str(input_list)}\nOutput:\n{output}\n\nProcessing Time: {proc_time}")
        print(f"Output: {output}")
        
        if not os.path.exists('Reading.csv'):
            with open('Reading.csv','w+') as file:
                print("File created.")
                
        with open('Reading.csv','a') as file:
            file.write(f"\n{algo},{input_type_string},Size: {input_list_size},Input: {' '.join(map(str,input_list))},Output: {' '.join(map(str,output))} , Time: {proc_time} seconds")


#     
# =============================================================================


input_algorithm=''
text1 = "1) Merge Sort\n2) Insertion Sort\n3) Selection Sort\n4) Bubble Sort\n5) Heap Sort\n6) Quick Sort(Regular)\n7) Quick Sort(Median Of Three)\nSelect algorithm number for sorting: "
input_list_size=''
text2= "Enter input size(max 999):\n"
input_type=''
input_type_string=''
text3 = "1) Ascending\n2) Descending\n3) Random\nSelect input type: "
input_list=[]

window = tk.Tk()
tk.Label(window, text=text1).grid(row=0)
tk.Label(window, text=text2).grid(row=1)
tk.Label(window, text=text3).grid(row=2)

input1 = tk.Entry(window)
input2 = tk.Entry(window)
input3 = tk.Entry(window)

input1.grid(row=0, column=1)
input2.grid(row=1, column=1)
input3.grid(row=2, column=1)

tk.Button(window, text='Sort', command=main_func).grid(row=3, column=1, sticky=tk.W, pady=4)

tk.mainloop()