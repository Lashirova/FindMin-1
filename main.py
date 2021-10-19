# lisOfIntegers =  [[5,2,31,9],[2,1,6,7,11],[55,1,7,8,9]]
# def minEl(listOfIntegers):
#     minimum = min(lisOfIntegers[0])
#     for i in lisOfIntegers:
#         miniMum = min(i)
#         if minimum > miniMum:
#          minimum = miniMum
#     return minimum
# print(minEl(lisOfIntegers))


# lisOfInt =  [[5,2,31,9],[2,1,6,7,11],[55,1,7,8,9]]
# for i in lisOfInt:
#     i.sort()
# def RetriveTheList(lisOfInt):
#     return [item[0] for item in lisOfInt]
# minimum = min(RetriveTheList(lisOfInt))
# print(minimum)


def findMin(nums):
  min=9999999
  for i in range(len(nums)):
    for j in range(len(nums[i])):
      if min>nums[i][j]:
        min=nums[i][j];

def findMinSorted(nums):
  min=9999999
  for i in range(len(nums)):
    nums[i].sort()
    if min>nums[i][0]:
      min=nums[i][0]

  return min

nums=[[5,2,31,9],[2,1,6,7,11],[55,1,7,8,9]]
print('Minimum with linear: ',findMin(nums))
print('Minimum with sort: ',findMinSorted(nums))
