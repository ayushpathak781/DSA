class Solution:
    def addTwoNumbers(self, head1, head2):
    #ayushpathak781
        temp1 = head1
        temp2 = head2
        new_head = ListNode(-1)
        dummy = new_head
        carry = 0

        while temp1 or temp2 or carry:

            s = carry
            if temp1:
                s += temp1.val
                temp1 = temp1.next
            if temp2:
                s += temp2.val
                temp2 = temp2.next

            carry = s // 10
            dummy.next = ListNode(s % 10)
            dummy = dummy.next

        return new_head.next