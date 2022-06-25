from pygorithm.data_structures.linked_list import SinglyLinkedList

print(SinglyLinkedList.get_code())


class SinglyLinkedList(object):
    """
    Defining the head of the linked list
    """

    def __init__(self):
        """
        constructor
        """
        self.head = None

    def _search(self, node, data):
        """
        searches the node, if valid returns the node else return false
        """
        if node is None:
            return False
        if node.data == data:
            return node
        return self._search(node.get_next(), data)

    def get_data(self):
        """
        prints the elements in the linked list
        """
        temp = self.head
        l_list = []
        while temp:
            l_list.append(temp.data)
            temp = temp.next

        return l_list

    def insert_at_start(self, data):
        """
        insert an item at the beginning of the linked list
        """
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, next_node_data, data):
        """
        insert an item after an element in the linked list
        """
        new_node = Node(data)
        current_node = self._search(self.head, next_node_data)
        new_node.next = current_node.next
        current_node.next = new_node

    def insert_at_end(self, data):
        """
        insert an item at the end of the linked list
        """
        new_node = Node(data)
        temp = self.head
        # get last node
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def delete(self, data):
        """
        to delete specified element from the linked list
        """
        temp = self.head
        # if data/key is found in head node itself
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                return
            else:
                # else search all the nodes
                while temp.next is not None:
                    if temp.data == data:
                        break
                    # save current node as previous so that we can go on to next node
                    prev = temp
                    temp = temp.next

                # node not found
                if temp is None:
                    return

                # TODO: local variable 'prev' might be referenced before assignment
                # TODO: Fix this
                prev.next = temp.next
                return

    @staticmethod
    def get_code():
        """
        return the code for the current class
        """
        return inspect.getsource(SinglyLinkedList)
