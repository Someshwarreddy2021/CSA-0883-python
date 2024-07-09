def remove_duplicates(input_list):
    return list(set(input_list))

if __name__ == "__main__":
   
    input_list = [1, 2, 3, 4, 5, 3, 2, 1, 6, 7, 8, 5, 9]
    
    unique_list = remove_duplicates(input_list)
    
    print("Original list:", input_list)
    print("List after removing duplicates:", unique_list)
