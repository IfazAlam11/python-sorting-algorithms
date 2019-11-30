#method 1
def bubbleSort(n):
  for x in range (0, len(n) - 1):
    if n[x] > n[x + 1]:
      swap_flag = True
      temp = n[x]
      n[x] = n[x + 1]
      n[x + 1] = temp
      
#method 2
def BubbleSort(nums):
  #counts number of swaps made
  swap_count = 0
    
  #scans the entire list
  for x in range(0,len(nums)-1):
    if nums[x] > nums[x+1]:
      #swaps the index values
      temp = nums[x]
      nums[x] = nums[x+1]
      nums[x+1] = temp
      swap_count += 1
  
  #recalls the function if swaps were made
  if swap_count > 0:
    return BubbleSort(nums)
  #returns the sorted list if no swaps were made throughout the entire list
  else:
    return nums
