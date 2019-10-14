class DoubleNode:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = None
        self.previous = None


if __name__ == "__main__":
    print("Creating a Linked List using class Node.")
    monday = DoubleNode("Monday")
    tuesday = DoubleNode("Tuesday")
    wednesday = DoubleNode("Wednesday")
    thursday = DoubleNode("Thursday")
    friday = DoubleNode("Friday")
    saturday = DoubleNode("Saturday")
    sunday = DoubleNode("Sunday")

    monday.next = tuesday

    tuesday.previous = monday
    tuesday.next = wednesday

    wednesday.previous = tuesday
    wednesday.next = thursday

    thursday.previous = wednesday
    thursday.next = friday

    friday.previous = thursday
    friday.next = saturday

    saturday.previous = friday
    saturday.next = sunday

    sunday.previous = saturday
    # sunday.next = monday #Uncomment this line and it will become a circular linked list

    current_node = monday
    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next
