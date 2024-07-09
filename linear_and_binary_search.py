def LinearSearch(number_list, number_to_find):
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index
    return -1

def BinarySearch(number_list, number_to_find):
    left_side = 0
    right_side = len(number_list)
    
    while left_side <= right_side:
        mid = (left_side + right_side) // 2
        mid_number = number_list[mid]
        
        if mid_number == number_to_find:
            return mid
        elif mid_number < number_to_find:
            left_side = mid + 1
        elif mid_number > number_to_find:
            right_side = mid - 1
    
    return -1


if __name__ == '__main__':
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number_to_find = 8
    
    index = LinearSearch(number_list, number_to_find)
    print(f'Linear Search found the element at position {index}')
    index1 = BinarySearch(number_list, number_to_find)
    print(f'Binary Search found the element at position {index1}')
