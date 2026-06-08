# data structures are used for organising data(save and retrieval)
# data structures are needed to store multiple data in a single variable

# num=[1,2,3]
# print(num[0])

name='akshat-raj'
# # a=len(name)
# b=len(name)//2
# print(a//2)
# print(a)

# i=0
# cnt=0
# while i<len(name):
#     if(name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u'):
#         cnt=cnt+1
#     i=i+1

# print(cnt)

# i=0
# cnt=0
# while i<len(name):
#     if(name[i]!='a' or name[i]!='e' or name[i]!='i' or name[i]!='o' or name[i]!='u'):
#         cnt=cnt+1
#     i=i+1

# print(cnt)
# cnt=0
# for x in name:
#     if( x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
#         cnt=cnt+1
# print(cnt)


cnt=0
for x in name:
    if( x!='a' or x!='e' or x!='i' or x!='o' or x!='u'):
        cnt=cnt+1
print(cnt)