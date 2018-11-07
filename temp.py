import ast
position = '(257, 37), (257, 37)'  # 目标：[(257, 37), (257, 37)]
position = position + ','
print(position)
str_tuple = ast.literal_eval(position)
print(str_tuple)
print(len(str_tuple))
tuple_list = list(str_tuple)
print(tuple_list)

position1 = '(257, 37)'     # 目标：[(257, 37)]
position1 = position1 + ','
print(position1)
str_tuple1 = ast.literal_eval(position1)
print(str_tuple1)
print(len(str_tuple1))
tuple_list1 = list(str_tuple1)
print(tuple_list1)
