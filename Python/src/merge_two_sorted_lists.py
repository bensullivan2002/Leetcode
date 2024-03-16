class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, list1, list2):
        merged_list_head = ListNode()
        merged_list_current = merged_list_head

        while list1 and list2:
            if list1.val < list2.val:
                merged_list_current.next = list1
                list1 = list1.next

            else:
                merged_list_current.next = list2
                list2 = list2.next

            merged_list_current = merged_list_current.next

        merged_list_current.next = list1 or list2

        return merged_list_head.next
