def subsequence(index,subarray,res):
   if index>=len(nums):
       if sum(subarray)==target:
           res.append(subarray.copy())
       return
   subarray.append(nums[index])
   subsequence(index+1,subarray,res)
   subarray.pop()
   subsequence(index+1,subarray,res)

nums = [5,9,4,3,1]
target = 9
subarray = []
result = []
print(subsequence(0,[],result))
print(result)