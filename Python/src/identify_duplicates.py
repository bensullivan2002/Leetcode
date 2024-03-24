def removeDuplicates(nums):
    char_tracker = {}
    k = 0

    for i in range(len(nums)):
        if nums[i] not in char_tracker:
            char_tracker.update({i: 1})
            k += 1
        if nums[i] in char_tracker:
            nums.pop(i)
            nums.append(None)
    return k

dummy = [1, 1, 2]
print(removeDuplicates(dummy))