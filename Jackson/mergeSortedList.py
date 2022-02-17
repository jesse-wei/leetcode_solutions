# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        t = self.merge(list1, list2)
        return t
    def merge(self, list1, list2):
        if list1 == None:
            # If you reach the end of list1, just return the rest of list2
            return list2
        if list2 == None:
            #If you reach the end of list2, just return the rest of list1
            return list1
        if list1.val < list2.val:
            # if list1's value is less than list2, then keep list1 and change its next value
            list1.next = self.merge(self, list1.next, list2)
            # return list1 whenever list1.val < list2.val
            return list1
            
        else:
            # if list2's value is less than or equal just keep list2 and change its next value
            list2.next = self.merge(self, list1, list2.next)
            return list2
            
#EXAMPLE [1,3]
"""[2,4]

list (1) less than list2(2)

keep list 1 
list1.next(3) = recurse with list1.next, since we are using list1
(return not evaluated yet)

now list1t(3) > list2(2)

list2.next(2)  = recurse with list2.next 
(return not evaluated yet)

list1(3) now less than list2 (4):
list1.next(None) = recurse with list1.next
return not evaluated
list == None
return list2 (4)
end of list2 now gets spliced with 
4 3 2 1

now it unravels 
return 3-->4
return 2-->3-->4
return 1--2->3-->4"""
""





