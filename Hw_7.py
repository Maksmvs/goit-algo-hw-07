class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max_value(node):
    if node is None:
        return float('-inf')

    left_max = find_max_value(node.left)
    right_max = find_max_value(node.right)

    return max(node.value, left_max, right_max)

def find_min_value(node):
    if node is None:
        return float('inf')

    left_min = find_min_value(node.left)
    right_min = find_min_value(node.right)

    return min(node.value, left_min, right_min)

def calculate_sum(node):
    if node is None:
        return 0

    left_sum = calculate_sum(node.left)
    right_sum = calculate_sum(node.right)

    return node.value + left_sum + right_sum

root = Node(1)
root.left = Node(5)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(8)
root.right.left = Node(6)
root.right.right = Node(9)

max_value = find_max_value(root)
min_value = find_min_value(root)
sum_values = calculate_sum(root)

print("Максимальне значення в дереві:", max_value)
print("Мінімальне значення в дереві:", min_value)
print("Сума всіх значень в дереві:", sum_values)



