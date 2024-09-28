class VerboseList(list):
    def append(self, item):
        # Call the original append method
        super().append(item)
        # Print a message after appending the item
        print(f"Added [{item}] to the list.")
    
    def extend(self, items):
        # Call the original extend method
        super().extend(items)
        # Print a message after extending the list
        print(f"Extended the list with [{len(items)}] items.")
    
    def remove(self, item):
        # Print a message before removing the item
        print(f"Removed [{item}] from the list.")
        # Call the original remove method
        super().remove(item)
    
    def pop(self, index=-1):
        # Print a message before popping the item
        item = self[index]
        print(f"Popped [{item}] from the list.")
        # Call the original pop method and return the item
        return super().pop(index)
