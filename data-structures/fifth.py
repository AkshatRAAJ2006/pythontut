# tuple datastructure
# tuple ds is immutable, no changes on it can be done

tp=(23,45,67,87,98,89)
# print(tp[0])
# midIndexVal=(len(tp))//2
# print(midIndexVal)
# print(tp[-1])



tpp=tp,1,23,45,67,'ign: soilderboy'
# print(tpp)
# print(len(tpp))


# i=0
# while i<len(tp):
#     print(tp[i])
#     i=i+1

# for x in tp:
#     print(x)


# i=0
# while i<len(tpp):
#     print(tpp[i])
#     i=i+1

# for x in tpp:
#     print(x)


# slicing is supported in tuple



i=0
while i<3:
    j=0
    while j<5:
        print(tpp[i][j])
        j=j+1
    i=i+1