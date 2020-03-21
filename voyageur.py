import itertools as it
#https://jmduke.com/posts/a-gentle-introduction-to-itertools/
letters = ['a', 'b', 'c', 'd', 'e', 'f']
booleans = [1, 0, 1, 0, 0, 1]
numbers = [23, 20, 44, 32, 7, 12]
decimals = [0.1, 0.7, 0.4, 0.4, 0.5]

#print list(it.chain(letters, booleans, decimals))
# print(*array, sep='')
print(*it.chain(letters, booleans, decimals))

# https://www.tutorialspoint.com/python3/python_lists.html
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])


data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
print(*it.accumulate(data, max))

print(*it.combinations('ABCD', 2))
# print(*it.permutations('1234567', 7))

matr = {}
matr[(0,0)] = 0
matr[(0,1)] = 15
matr[(0,2)] = 5
matr[(0,3)] = 16


matr[(1,0)] = 10
matr[(1,1)] = 0
matr[(1,2)] = 12
matr[(1,3)] = 11


matr[(2,0)] = 13
matr[(2,1)] = 9
matr[(2,2)] = 0
matr[(2,3)] = 8


matr[(3,0)] = 6
matr[(3,1)] = 14
matr[(3,2)] = 8
matr[(3,3)] = 0


print(matr[(0,0)])

# def davy_accumulate(iterable):
#     return matr[(int(elt1), int(elt2))]


def davy_accumulate(iterable):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], operator.nul)  --> 1 2 6 24 120
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    elt_prec="0"
    total0=0
    for element in it:

        dist = matr[(int(elt_prec),int(element))]
        total0 = total0+dist
        elt_prec=element
        yield total0

min_all=10000000000000000000001
min_trouve=10000000000000000000001
#for i in it.permutations('1234567', 7):
for i in it.permutations('123', 3):
    a=tuple('0')+i+tuple('0')
    print ("a :", a)
    response = list(davy_accumulate(a))
    min_all=min(min_all,response[4])
    if response[4] < min_trouve: #Si a est positif
        min_trouve=response[4]
        chemin_trouve=a

    # print(*davy_accumulate(a))
print ("min_trouve :", min_trouve)

print ("chemin_trouve :", chemin_trouve)
