# lisOfInt =  [[5,2,31,9],[2,1,6,7,11],[55,1,7,8,9]]
# def minEl(listOfInt):
#     minimum = min(lisOfInt[0])
#     for i in lisOfInt:
#         miniMum = min(i)
#         if minimum > miniMum:
#          minimum = miniMum
#     return minimum
# print(minEl(lisOfInt))

lisOfInt =  [[5,2,31,9],[2,1,6,7,11],[55,1,7,8,9]]
for i in lisOfInt:
    i.sort()
def RetriveTheList(lisOfInt):
    return [item[0] for item in lisOfInt]
minimum = min(RetriveTheList(lisOfInt))
print(minimum)