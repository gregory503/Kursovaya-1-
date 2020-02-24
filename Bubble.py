def bubble_sort(nums):  
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True
# Verify it works
random_list_of_nums = [2, 3, 7, 11, 15, 22, 77, 98, 112, 55, 66, 17, 98, 18, 27, 29, 37, 48, 31, 58]  
bubble_sort(random_list_of_nums)  
print(random_list_of_nums) 
