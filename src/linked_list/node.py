class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


if __name__ == "__main__":
    print("Creating a Linked List using class Node.")
    monday = Node("Monday")
    tuesday = Node("Tuesday")
    wednesday = Node("Wednesday")
    thursday = Node("Thursday")
    friday = Node("Friday")
    saturday = Node("Saturday")
    sunday = Node("Sunday")

    monday.next = tuesday
    tuesday.next = wednesday
    wednesday.next = thursday
    thursday.next = friday
    friday.next = saturday
    saturday.next = sunday
    # sunday.next = monday #Uncomment this line and it will become a circular linked list

    current_node = monday
    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next
