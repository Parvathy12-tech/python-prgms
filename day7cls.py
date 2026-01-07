
grocery_list = ["milk", "bread", "eggs"]


def add_item(item):
    grocery_list.append(item)


def remove_last_item():
    if grocery_list:
        grocery_list.pop()


display_item = lambda item: print("Item:", item)


def count_characters(items):
    if not items:
        return 0
    return len(items[0]) + count_characters(items[1:])


add_item("rice")
remove_last_item()
for item in grocery_list:
    display_item(item)

print("Total characters:", count_characters(grocery_list))