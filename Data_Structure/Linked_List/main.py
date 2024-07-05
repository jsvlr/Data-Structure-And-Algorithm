# The class `Node` represents a node in a linked list with a data attribute and a reference to the
# next node.
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# This Python class represents a linked list with methods for updating and deleting nodes.
class LinkedList:
    def __init__(self) -> None:
        self.head:Node | None = None
        self.tail:Node | None = None
        # private variable to keep track of the index that will pass in update and delete method
        self._length = 0 

    # method to get the lenght of the list
    def getLength(self) -> int:
        return self._length
    
    # method to insert node. (the index is for specific index of the list)
    def insertNode(self, node:Node, index:int|None = None) -> None:
        
        # check if there is a value for index and not exceed in the current value of linked list lenght
        if index is not None and index > self._length:
            raise ValueError("Index out of bounds")
        
        # store new node in variable
        createdNode = Node(node)

        # condition to set the head as new node if the head is None
        if self.head is None:
            self.head = createdNode
            # update the value of lenght
            self._length += 1
            # exit code block
            return
        
        # if index = 0 then it is the new head of the linked list
        if index == 0:
            self.head, createdNode.next = createdNode, self.head
            # update the value of lenght
            self._length += 1
            # exit code block
            return
        
        # set as current node
        currentNode = self.head
        
        if index is None:
            # this loop will iterate over the nodes until find the tail of Linked List
            while currentNode is not None:
                if currentNode.next == None:
                    currentNode.next = Node(node)
                    # Update the value of tail. End of the Linked List
                    self.tail = createdNode
                    # update the value of lenght
                    self._length += 1
                    return
                currentNode = currentNode.next
        else:
            # variable to check the position
            count = 0
            # will loop until the current node is not none and the count not exceed the lenght
            while currentNode is not None and count < self._length:
                if count == index - 1:
                    # swap the position of the node
                    # current = new_node
                    # new_node.next = current
                    currentNode.next, createdNode.next = createdNode, currentNode.next
                    
                    # update the tail 
                    if createdNode.next is None:
                        self.tail = createdNode

                    # update the value of lenght
                    self._length += 1
                currentNode = currentNode.next
                count += 1

    # method to update a node
    def updateNode(self, index:int, data) -> None:
        if index > self._length:
            raise ValueError("Index out of bounds")
        
        currentNode = self.head

        # variable to check the current index
        counter = 0
        while currentNode is not None:
            if counter == index:
                # assign the data pass as new data on current node
                currentNode.data = data
                # exit the code
                return
            
            # update the currentNode variable
            currentNode = currentNode.next

            # update the counter by adding 1
            counter += 1
    
    # method to delete a node
    def deleteNode(self, index:int|None = None) -> None:
        if index is not None:
            if index > self._length:
                raise ValueError("Index out of bounds")
        
        if index == 0:
            self.head = self.head.next
            # update the lenght of linked list
            self._length -= 1
            # exit code block
            return

        # update the lenght of linked list
        self._length -= 1

        currentNode = self.head
        # variable to check the current index
        counter = 0 
        if index is not None:
            while currentNode is not None:
                # check if the current counter is the same in index
                if counter + 1 == index:
                    currentNode.next = currentNode.next.next
                    # update the tail
                    if currentNode.next is None:
                        self.tail = currentNode
                    return
                # update the currentNode variable
                currentNode = currentNode.next
                # update the counter by adding 1
                counter += 1
        else:
            # loop that will check 2 preceeding node if next is none
            while currentNode.next.next is not None:
                # update the value of current node
                currentNode = currentNode.next
            # update the tail node
            self.tail = currentNode
            # set the tail of the node to none
            currentNode.next = None

    # method to print all data(s) in Nodes
    def printNode(self) -> None:
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data if currentNode.next is None else f"{currentNode.data} -> ", end = "")
            currentNode = currentNode.next

    # method to return string representation of this class
    def __str__(self) -> str:
        headValue = self.head.data if self.head is not None else None
        tailValue = self.tail.data if self.tail is not None else None
        lenghtValues = self._length
        return f"Head: {headValue}\nTail: {tailValue}\nLenght: {lenghtValues}"


def main() -> None:
    # set instance of the Linked List
    linked = LinkedList()
    sampleDatas = [1, 'Hello, World!', 2, 3, 4, 5]

    # loop to set the nodes 
    for data in sampleDatas:
        linked.insertNode(data)

    # insert node 
    # if the index is not specified then it will place on tail 
    linked.insertNode(index = 0, node = 'Im on Head')
    linked.insertNode(node = 'Im on Tail')

    # update node
    linked.updateNode(index = 0, data = 'Updated Head')

    linked.deleteNode(index = 2)
    # print the nodes
    linked.printNode()

if __name__ == "__main__":
    main()

