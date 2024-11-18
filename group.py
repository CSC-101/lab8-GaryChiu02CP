def groups_of_3(array:list[int]) -> list[list[int]]:
    narray = []
    for i in range(0,len(array),3):
        narray.append([array[i],array[i+1],array[i+2]])
    return narray

