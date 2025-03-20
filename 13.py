def removeDuplicate(self):
    uniqueList = []
    for item in self:
        if item not in uniqueList:
            uniqueList.append(item)
    return uniqueList


list = [1,1,11,1,2,2,3,3,4,5,6,6,7,7,8,8,9,9]
print(removeDuplicate(list))