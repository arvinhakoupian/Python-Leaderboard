class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empthy")

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
        
    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index< 0 or index>=self.get_lenght():
            raise Exception("Invalid index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

ll = LinkedList()
ll.insert_at_beginning("apple")
ll.insert_at_beginning("mango")
ll.insert_at_beginning("pinapple")
ll.insert_at_end("orange")
ll.insert_values(["xndzor","tandz"])
try:
    ll.remove_at(1)
except:
    print("error")
print(ll.get_lenght())
ll.print()
ll.print()