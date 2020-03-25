from node import Node


class Tree:
    """The class used to represent the binary tree"""

    def __init__(self, root_value):
        self.root = Node(root_value)
        self.sum = 0
        self.average = 1  # meter to help counting the average
        self.median = []  # list of value of each node in subtree

    def insert(self, data, node, left_or_right):

        if node:
            if left_or_right is "left":
                node.left = Node(data)
                return node.left
            elif left_or_right is "right":
                node.right = Node(data)
                return node.right
            else:
                raise ValueError("Left_or_right argument value is invalid")
        else:
            raise Exception('Existing node')

    def calculate_sum(self, node):
        self.sum = 0
        self._calculate_sum(node)
        return self.sum

    def _calculate_sum(self, node):
        if node is None:
            return None
        else:
            self.sum += node.value
            self._calculate_sum(node.left)
            self._calculate_sum(node.right)

    def calculate_average(self, node):
        self.average = 0
        self._calculate_average(node)
        subtree_sum = self.calculate_sum(node)
        if self.average != 0:
            average = subtree_sum / self.average
            return average
        else:
            return 0

    def _calculate_average(self, node):
        if node is None:
            return None
        else:
            self.average += 1
            self._calculate_average(node.left)
            self._calculate_average(node.right)

    def calculate_median(self, node):
        self.median = []
        result = self._calculate_median(node)
        if result:
            self.median.sort()
            if len(self.median) == 1:
                return self.median[0]
            elif len(self.median) % 2 == 1:
                return self.median[int(len(self.median) / 2)]
            else:
                return (self.median[int(len(self.median) / 2)] + self.median[int(len(self.median) / 2) - 1]) / 2
        else:
            return None

    def _calculate_median(self, node):
        if node is None:
            return False
        else:
            self.median.append(node.value)
            self._calculate_median(node.left)
            self._calculate_median(node.right)
            return True
