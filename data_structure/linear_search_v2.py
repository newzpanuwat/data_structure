# or sequence search
search_names = ['Cola', 'Kaka', 'Company', 'Siri']


def index_of_item(collection, target):
    for i in range(0, len(collection)):
        if target == collection[i]:
            return i
    return None

for n in search_names:
    index = index_of_item(search_names, n)
    print(index)