from Node import Node


class LinkedList:

    def insert(self, head, new_data):
        if head.data is None:
            head.data = new_data
            return
        else:
            p = head
            while p:
                if p.next is None:
                    p.next = Node(new_data)
                    return
                else:
                    p = p.next

    def printLL(self, head):
        if head is None:
            return "Empty LinkedList."
        while head:
            print(head.data, end=" ")
            head = head.next

    def findFormLast(self, head, n):
        if head is None:
            return "Empty LL."
        else:
            p = head
            q = head

            for i in range(0, n-1):
                if q.next:
                    q = q.next
                else:
                    return "No element from last."

            while q:
                if q.next is not None:
                    p = p.next
                    q = q.next
                else:
                    return p.data


if __name__ == '__main__':
    ll = LinkedList()
    head = Node(None)
    ll.insert(head, 20)
    ll.insert(head, 30)
    ll.insert(head, 40)
    ll.insert(head, 50)
    ll.insert(head, 60)
    ll.insert(head, 70)


    ll.printLL(head)

    print()

    print(ll.findFormLast(head, 3))