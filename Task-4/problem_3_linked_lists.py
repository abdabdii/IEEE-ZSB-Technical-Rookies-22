class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def length(self):
        curr = self.head
        count = 0
        while curr.next != None:
            count += 1
            curr = curr.next
        return count

    def getAll(self):
        nodes = []
        curr = self.head
        while curr.next != None:
            curr = curr.next
            nodes.append(curr.data)
        return nodes

    def insert(self, data, index):
        new_node = Node(data)
        curr = self.head
        curr_index = 0
        while True:
            last_node = curr
            curr_node = curr.next
            if curr_index == index:
                last_node.next = new_node
                new_node.next = curr_node
                return
            curr = last_node.next
            curr_index += 1

    def delete(self, index):
        curr_index = 0
        curr = self.head
        while True:
            last_node = curr
            curr_node = curr.next
            if curr_index == index:
                last_node.next = curr_node.next
                return
            curr = last_node.next
            curr_index += 1


def getOccurs(curr_node, target):
    if curr_node == None:
        return 0
    count = getOccurs(curr_node.next, target)
    if curr_node.data == target:
        return count + 1
    else:
        return count


# linkedList = LinkedList()
# linkedList.append(5)
# linkedList.append(3)
# linkedList.append(4)
# linkedList.append(4)
# linkedList.append(4)
# linkedList.insert(9, 2)
# linkedList.delete(2)
# print(getOccurs(linkedList.head, 4))
# print(linkedList.getAll())
