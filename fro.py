from collections import Counter
def DicSum(d1, d2):
    sum = dict(Counter(d1) + Counter (d2))
    return sum
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}
sumOfDic = DicSum(dict1 , dict2)
print(sumOfDic)

