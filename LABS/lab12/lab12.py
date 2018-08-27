"""
Tara Walton // tara1984
Lab 12 - Due 5/7/15

Description - append, display and other practice with singly linked nodes
"""

from node import Node 

class SinglyLinkedStructure(object):
    def __init__(self, seq=None):
        '''accepts head and size'''
        self.head = None
        self.size = 0
        if seq != None:
            for value in seq:
                self.append(value)

    def append(self, val):
        '''appends a new node to the end of the structure'''
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            probe = self.head
            while probe.next != None:
                probe = probe.next
            probe.next = newNode
        self.size+=1
            
    def __len__(self):
        '''returns the number of nodes'''
        return self.size

    def __str__(self):
        '''returns a string representation of structure'''
        result = ''
        if self.head == None:
            return result
        else:
            probe = self.head
            while probe.next != None:
                result += str(probe.data) + ' '
                probe = probe.next
            result += str(probe.data)
            return result

        
#code below by Dr. Jamil Saquer
def main():
    l1 = SinglyLinkedStructure()
    print('Empty singly linked structure')
    print(l1)
    print(len(l1))
    print()
    
    l1.append('Hello,')
    l1.append('how')
    l1.append('are')
    l1.append('you?')
    print(l1)
    print(len(l1))
    print()
    
    seq = list(range(1, 6))
    l2 = SinglyLinkedStructure(seq)
    print(l2)
    print(len(l2))
    print()

    t = tuple([x*10 for x in seq])
    print(t)
    print()

    l2 = SinglyLinkedStructure(t)
    print(l2)
    print(len(l2))
    print()

    l2 = SinglyLinkedStructure("abcxyz")
    print(l2)
    print(len(l2))
    
main()
