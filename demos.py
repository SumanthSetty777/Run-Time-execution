# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 22:11:31 2021

@author: sumanthsetty
"""


#Quick Sort
def quick_sort(arr):
    
        
    if len(arr)<2:
        return arr
    else:
        pivot=arr[-1]
        smaller,larger,equal=[],[],[]
        for num in arr:
            if num<pivot:
                smaller.append(num)
            elif num==pivot:
                equal.append(num)
            else:
                larger.append(num)
        return(quick_sort(smaller) + equal + quick_sort(larger))
        
        return()
# End of Quick Sort
        
#Merge Sort
def merge_sorted(arr1,arr2):
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr

def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = merge_sort(arr[:middle])
        l2 = merge_sort(arr[middle:])
        return merge_sorted(l1, l2)
#End of Merge Sort
       
#Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr)):#while is more efficient here
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1] = arr[i+1],arr[i]
    
        
#End of Bubble Sort
    
#Selection Sort
def selection_sort(arr):
    spot_marker = 0
    while spot_marker<len(arr):
        for i in range(spot_marker,len(arr)):
            if(arr[i]<arr[spot_marker]):
                arr[spot_marker],arr[i] = arr[i],arr[spot_marker] 
        spot_marker+=1
#End of Selection Sort
            
#Insertion Sort
def insertion_sort(arr):
    for key in range(1, len(arr)):
        if arr[key] < arr[key-1]:
            j = key
            while j > 0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
#End of Insertion Sort