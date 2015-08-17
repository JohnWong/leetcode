class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        t1 = l1
        t2 = l2
        flag = 0
        while t1 is not None:
            if t2 == None:
                t1.val += flag
            else:
                t1.val += t2.val + flag
                pass
            if t1.val >= 10:
                flag = 1
                t1.val -= 10
            else:
                flag = 0
                pass
            if t1.next is None and t2 is not None and t2.next is not None:
                t1.next = t2.next
                t2.next = None
                pass
            if flag == 1 and t1.next is None:
                t1.next = ListNode(flag)
                break
            else:
                t1 = t1.next
                pass
            t2 = t2.next if t2 is not None else None
            pass
        return l1