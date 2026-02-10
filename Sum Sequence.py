def sum_subseqence(index,total,subset):
   if total == target:
       result.append(subset.copy())
       return
   elif total>target:
       return
   if index>=len(nums):
       return

   #included
   subset.append(nums[index])
   sum = total + nums[index]
   sum_subseqence(index+1,sum,subset)

   #exculding
   e = subset.pop()
   sum = sum-e
   sum_subseqence(index+1,sum,subset)


nums=[5,9,4,3,1]
target = 9
result = []

sum_subseqence(0,0,[])
print(result)