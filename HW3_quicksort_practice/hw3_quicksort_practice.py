#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 16 14:41:41 2025

@author: linyixuan
"""

def quicksort (arr,start,end):
    if start >= end:
        return
    
    pivot = start
    left = start +1
    right = end
    
    print(f"\n[排續過程] :{arr[start:end+1]}，基準點：{arr[pivot]}")
    
    while left <= right:
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            print(f"交換 left:{arr[left]} 和 right:{arr[right]} -> {arr}")

    arr[pivot], arr[right] = arr[right], arr[pivot]
    print(f"交換 pivot:{arr[pivot]} 和 right:{arr[right]} -> {arr}")
    
    quicksort(arr, start, right - 1)
    quicksort(arr, right + 1, end)


user_input = input("請輸入一串數字（以空格或逗號分隔）：\n")

arr = [int(x) for x in user_input.replace(',', ' ').split()]
print(f"\n原始陣列: {arr}")
quicksort(arr, 0, len(arr) - 1)

print(f"\n[排序結束] 最終結果: {arr}")