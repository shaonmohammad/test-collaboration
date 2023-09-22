class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class Linked_List: 
    def __init__(self):
        self.head = None
        
    def insert_at_head(self,data):
        node = Node(data, self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print('Linked List is empty')
            return
        
        itr = self.head
        llstr = ''
        
        while itr:
            llstr += str(itr.data) + '-->'   
            itr = itr.next
        
        print (llstr)
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None)
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

if __name__ == '__main__':
    ll = Linked_List()
    # ll.insert_at_end(20)
    # ll.insert_at_end(203)
    # ll.insert_at_end(202)
    ll.insert_values(["Apple", "Mango", "Orange"])
    ll.print()