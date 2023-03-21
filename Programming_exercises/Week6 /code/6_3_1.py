class ToDoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} added to the to-do list.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} removed from the to-do list.")
        else:
            print(f"{item} is not in the to-do list.")

    def check_item(self, item):
        if item in self.items:
            print(f"{item} is in the to-do list.")
        else:
            print(f"{item} is not in the to-do list.")

    def print_list(self):
        print("To-Do List:")
        for item in self.items:
            print(f"- {item}")

    def get_list(self):
        return self.items