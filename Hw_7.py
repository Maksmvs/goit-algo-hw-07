class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max_value(node):
    # Базовий випадок: якщо вузол порожній, повертаємо негативну нескінченність
    if node is None:
        return float('-inf')

    # Рекурсивно знаходимо максимальне значення в лівому та правому піддеревах
    left_max = find_max_value(node.left)
    right_max = find_max_value(node.right)

    # Порівнюємо значення в поточному вузлі з максимальними значеннями в піддеревах
    return max(node.value, left_max, right_max)

def find_min_value(node):
    # Базовий випадок: якщо вузол порожній, повертаємо позитивну нескінченність
    if node is None:
        return float('inf')

    # Рекурсивно знаходимо мінімальне значення в лівому та правому піддеревах
    left_min = find_min_value(node.left)
    right_min = find_min_value(node.right)

    # Порівнюємо значення в поточному вузлі з мінімальними значеннями в піддеревах
    return min(node.value, left_min, right_min)

def calculate_sum(node):
    # Базовий випадок: якщо вузол порожній, повертаємо 0
    if node is None:
        return 0

    # Рекурсивно знаходимо суму значень в лівому та правому піддеревах
    left_sum = calculate_sum(node.left)
    right_sum = calculate_sum(node.right)

    # Додаємо значення поточного вузла до суми
    return node.value + left_sum + right_sum

# Приклад використання
# Створюємо дерево:
#       1
#      / \
#     5   3
#    / \ / \
#   4  8 6  9

root = Node(1)
root.left = Node(5)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(8)
root.right.left = Node(6)
root.right.right = Node(9)

# Знаходимо найбільше, найменше та суму значень в дереві
max_value = find_max_value(root)
min_value = find_min_value(root)
sum_values = calculate_sum(root)

print("Найбільше значення в дереві:", max_value)
print("Найменше значення в дереві:", min_value)
print("Сума всіх значень в дереві:", sum_values)

