# class Solution:
#     def twoSum(self, nums, target):
#         result = [(nums.index(num), nums.index((target-num))) for num in nums if (target-num) in nums[num:]]
#         answer = []
#         for i in result:
#             for j in i:
#                 answer.append(j)
#         return answer


# solution = Solution()
# print(solution.twoSum([3, 2, 4], 6))


class Solution:
    def twoSum(self, nums, target):
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i


solution = Solution()
answer = solution.twoSum([2, 7, 11, 15], 9)
print(answer)