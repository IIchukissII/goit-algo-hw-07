class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def get_height(self):
        if not self:
            return 0
        return self.height

    def update_height(self):
        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0
        self.height = 1 + max(
            left_height, right_height
        )

    def get_balance(self):
        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0
        return left_height - right_height

    def left_rotate(self):
        new_root = self.right
        t = new_root.left

        new_root.left = self
        self.right = t

        self.update_height()
        new_root.update_height()

        return new_root

    def right_rotate(self):
        new_root = self.left
        t = new_root.right

        new_root.right = self
        self.left = t

        self.update_height()
        new_root.update_height()

        return new_root

    def find_min_value_node(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def insert_node(self, key):
        if key < self.key:
            if self.left:
                self.left = self.left.insert_node(key)
            else:
                self.left = AVLNode(key)
        elif key > self.key:
            if self.right:
                self.right = self.right.insert_node(key)
            else:
                self.right = AVLNode(key)
        else:
            return self

        self.update_height()

        balance = self.get_balance()

        if balance > 1:
            if key < self.left.key:
                return self.right_rotate()
            else:
                self.left = self.left.left_rotate()
                return self.right_rotate()

        if balance < -1:
            if key > self.right.key:
                return self.left_rotate()
            else:
                self.right = self.right.right_rotate()
                return self.left_rotate()

        return self

    def delete_node(self, key):
        if not self:
            return self

        if key < self.key:
            self.left = self.left.delete_node(key)
        elif key > self.key:
            self.right = self.right.delete_node(key)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                temp = self.right.find_min_value_node()
                self.key = temp.key
                self.right = self.right.delete_node(temp.key)

        self.update_height()

        balance = self.get_balance()

        if balance > 1:
            if key < self.left.key:
                return self.right_rotate()
            else:
                self.left = self.left.left_rotate()
                return self.right_rotate()

        if balance < -1:
            if key > self.right.key:
                return self.left_rotate()
            else:
                self.right = self.right.right_rotate()
                return self.left_rotate()

        return self

    def sum_all_nodes(self):
        total = self.key
        if self.left:
            total += self.left.sum_all_nodes()
        if self.right:
            total += self.right.sum_all_nodes()
        return total

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def main():
    root = AVLNode(10)
    keys = [20, 30, 25, 19, 27, -1, -2, 18]
    print("======" * 3 + "Завдання 1" + "=======" * 3)
    for key in keys:
        root = root.insert_node(key)
        print("Inserted:", key)
    print(root)

    keys_to_delete = [10, 27]
    for key in keys_to_delete:
        root = root.delete_node(key)
        print("Deleted:", key)
    print(root)

    print("======"*3 + "Завдання 2" + "======="*3)
    print("Minimum value node:", root.find_min_value_node())
    print("======" * 3 + "Завдання 3" + "=======" * 3)
    print("Sum of all nodes:", root.sum_all_nodes())


if __name__ == "__main__":
    main()
