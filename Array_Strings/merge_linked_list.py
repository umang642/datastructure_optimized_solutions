from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeLinkedList:
    def get_merged_linked_list(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> ListNode:
        # get the dummynode 
        dummy = ListNode()
        tail = dummy 

        while list1 and list2: 
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        if list1:
            tail.next = list1
        
        if list2:
            tail.next = list2
        
        return dummy.next
    

if __name__ == '__main__':
    list1 = [1,2,4]
    list2 = [1,3,5]
    s = MergeLinkedList()
    print(s.get_merged_linked_list(list1=list1, list2=list2))
