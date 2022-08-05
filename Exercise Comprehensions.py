some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

#duplicates = []
#for value in some_list:
#    if some_list.count(value) > 1:
#        if value not in duplicates:
#            duplicates.append(value)
duplicates = []
duplicates = set([v for v in some_list if some_list.count(v) > 1 if v not in duplicates])
print(duplicates)