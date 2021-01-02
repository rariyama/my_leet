import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return new_head


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.data = [
            ListNode(
                val=1,
                next=ListNode(
                    val=2,
                    next=ListNode(
                        val=3,
                        next=ListNode(
                            val=4,
                            next=ListNode(
                                val=5,
                                next=None
                            )
                        )
                    )
                )
            ),
            [5,4,3,2,1]
        ]

    def test_reverse_linked_list(self):
        res = Solution().reverseList(self.data[0])
        self.assertEqual(self.data[1][0], res.val)
        self.assertEqual(self.data[1][1], res.next.val)
        self.assertEqual(self.data[1][2], res.next.next.val)
        self.assertEqual(self.data[1][3], res.next.next.next.val)
        self.assertEqual(self.data[1][4], res.next.next.next.next.val)


if __name__ == '__main__':
    unittest.main()
