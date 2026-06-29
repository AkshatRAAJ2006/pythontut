# logical data structures
# Stack(LIFO)
# follows LIFO principle-----> Last in First Out
# the first data to be inserted is the first one to be taken out



# custom function for length
# nums=[1,2,3,4,5,6]

# def lenx():
#     count=0
#     for x in nums:
#         count=count+1
#     return count


# print(lenx(nums))



# num=[1,2,3,4]


# def cnt(num):
#     cnt=0
#     i=0
#     while(i<len(num)):
#         cnt=cnt+1
#         i=i+1
#     return cnt


# print(cnt([2,4,6,8,8,9]) -1)

# num=[1,2,3,4,5]

# def reverseFn(num):
#     i=len(num)-1
#     while i>=0:
#         print(num[i])
#         i=i-1


# nums=[2,3,4,5,6,7,8]
# print(reverseFn(nums))
# print(nums)

# nums=[
#     [
#     [10,20,30],
#     [40,50,60],
#     [70,80,90],
#     ]]

# i=0
# while (i<1):
#     j=0
#     while(j<3):
#         k=0
#         while(k<3):
#             print(nums[i][j][k])
#             k=k+1
#         j=j+1
#     i=i+1


# print(nums.index(2))

# nums=[23,43,5,6,34,54,56,43,56,34]

# def custom_reverse(nums):
#     start=0
#     end=len(nums)-1
#     while(start<end):
#         nums[start],nums[end]=nums[end],nums[start]
#         start=start+1
#         end=end-1
        
# custom_reverse(nums)


# print(nums)