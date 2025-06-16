def subtract_list(check_list: list, must_be_in: list) -> list:
    return [element for element in check_list if element not in must_be_in]


#print(subtract_list([3,5,6,7,1], [1,2,3,4,5])) -> [6,7]
#print(subtract_list([1,3,5,6,7,8], [1,3,5])) -> [6, 7, 8]
