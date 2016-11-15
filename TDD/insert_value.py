def insert_val_at(index, my_list, value):
    for item in range(0, len(my_list)):
        if item == index:
            my_list.insert(index, value)
            return my_list
        elif item > len(my_list):
            return False
# print(insert_val_at(2, [1,2,3,4,5,6], 8))

# insert_val_at(2, self.test_list, 100)
