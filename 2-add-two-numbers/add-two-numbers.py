class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        tail = dummy

        carry = 0

        while l1 is not None or l2 is not None:

            if l1 is not None:
                a = l1.val
            else:
                a = 0

            if l2 is not None:
                b = l2.val
            else:
                b = 0

            total = a + b + carry

            carry = total // 10
            digit = total % 10

            new_node = ListNode(digit)

            tail.next = new_node
            tail = tail.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        if carry:
            tail.next = ListNode(carry)

        return dummy.next