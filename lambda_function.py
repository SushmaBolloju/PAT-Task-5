my_list = [1,'aadhya',35,'is my world',5]

#integer is added to list if given item is integer else string is added.
list_item_types = list(map(lambda x: 'integer' if isinstance(x, int) else 'string', my_list))

print(list_item_types)
