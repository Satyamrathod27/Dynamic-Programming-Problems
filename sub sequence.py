def subsequences(index, subarray, result):
   if index >= len(nums):
       if sum(subarray) == target:
           result.append(subarray.copy())
       return

   # include
   subarray.append(nums[index])
   subsequences(index + 1, subarray, result)
   subarray.pop()

   # exclude
   subsequences(index + 1, subarray, result)


nums = [5, 9, 4, 3, 1]
target = 9
res = []
subsequences(0, [], res)
print(res)