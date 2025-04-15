# Add your clarifying questions here

def rotate_list(list, shift_by):
    if shift_by > len(list) + 1:
        shift_by = shift_by % len(list)
    new_list = [num for num in list]
    for index in range(len(list)):
        new_list[index - (shift_by - 1)] = list[index]
    return new_list

print("\nfirst implementation:")
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 6))
print(rotate_list([1, 2, 3, 4, 5], 7))

def rotate_list(list, shift_by):
    shift_by %= len(list)
    return list[-shift_by:] + list[:-shift_by]

print("\nsecond implementation:")
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 7))
print(rotate_list([45, 3, 7, 25, 10], 3))

# def rotate_list(list, shift_by):
#     if shift_by > len(list) + 1:
#         shift_by = shift_by % len(list)
#     val_to_move = 0
#     for index in range(len(list)):
#         list.append(list[index - (shift_by - 1)])

# iterate through list backwards
# start at index 4
# save value at index 4 (which is 5)
# value 5 is now supposed to be at index 2 (len(list) - shift_by)

def rotate_list(list, shift_by):
    shift_by %= len(list)
    for _ in range(shift_by):
        list.insert(0, list.pop())
    return list 

print("\nthird implementation:")
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 7))
print(rotate_list([1, 2, 3, 4, 5], -4))
print(rotate_list([45, 3, 7, 25, 10], 3))
