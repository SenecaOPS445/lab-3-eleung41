#!/usr/bin/env python3
# Author ID: 147724231

# Declare the initial list called my_list
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Appends new item to the end of the list with the value (last item + 1)
    new_item = ordered_list[-1] + 1  # Get the last item and add 1
    ordered_list.append(new_item)  # Append the new item to the list

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values found in items_to_remove list from ordered_list
    for item in items_to_remove:
        if item in ordered_list:
            ordered_list.remove(item)  # Remove the item from the list if it exists

# Main code
if __name__ == '__main__':
    print(my_list)  # Print the initial list
    add_item_to_list(my_list)  # Add an item to the list
    add_item_to_list(my_list)  # Add another item to the list
    add_item_to_list(my_list)  # Add one more item to the list
    print(my_list)  # Print the updated list
    remove_items_from_list(my_list, [1, 5, 6])  # Remove specified items from the list
    print(my_list)  # Print the final modified list

