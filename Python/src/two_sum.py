def create_list_of_indices(i, num, num_to_index, target):
    return [i, num_to_index[target - num]]


def not_same_num(i, num, num_to_index, target):
    return num_to_index[target - num] != i


def delta_in_nums(num, num_to_index, target):
    return (target - num) in num_to_index


def populate_hashmap_of_nums(delta_and_index, nums):
    for i, num in enumerate(nums):
        delta_and_index[num] = i


class Solution:
    def two_sum(self, nums, target):
        num_to_index = {}

        populate_hashmap_of_nums(num_to_index, nums)

        for i, num in enumerate(nums):
            if delta_in_nums(num, num_to_index, target) and not_same_num(i, num, num_to_index, target):
                return create_list_of_indices(i, num, num_to_index, target)
