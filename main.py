class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

    @staticmethod
    def get_height(node):
        return node.height if node else 0

    @staticmethod
    def get_balance(node):
        return (
            AVLNode.get_height(node.left) - AVLNode.get_height(node.right)
            if node
            else 0
        )

    @staticmethod
    def left_rotate(node_z):
        node_y = node_z.right
        T2 = node_y.left

        node_y.left = node_z
        node_z.right = T2

        node_z.height = 1 + max(AVLNode.get_height(node_z.left), AVLNode.get_height(node_z.right))
        node_y.height = 1 + max(AVLNode.get_height(node_y.left), AVLNode.get_height(node_y.right))

        return node_y

    @staticmethod
    def right_rotate(y):
        x = y.left
        T3 = x.right

        x.right = y
        y.left = T3

        y.height = 1 + max(AVLNode.get_height(y.left), AVLNode.get_height(y.right))
        x.height = 1 + max(AVLNode.get_height(x.left), AVLNode.get_height(x.right))

        return x

    @staticmethod
    def find_min_value_node(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def insert_node(self, key):
        if not self:
            return AVLNode(key)

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

        self.height = 1 + max(
            self.get_height(self.left) if self.left else 0, self.get_height(self.right) if self.right else 0
        )

        balance = self.get_balance(self)

        if balance > 1:
            if key < self.left.key:
                return self.right_rotate()
            else:
                self.left = self.left_rotate()
                return self.right_rotate()

        if balance < -1:
            if key > self.right.key:
                return self.left_rotate()
            else:
                self.right = self.right_rotate()
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
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            temp = AVLNode.find_min_value_node(self.right)
            self.key = temp.key
            self.right = self.delete_node(self.right, temp.key)

        if self is None:
            return self

        self.height = 1 + max(
            AVLNode.get_height(self.left), AVLNode.get_height(self.right)
        )

        balance = AVLNode.get_balance(self)

        if balance > 1:
            if AVLNode.get_balance(self.left) >= 0:
                return AVLNode.right_rotate(self)
            else:
                self.left = AVLNode.left_rotate(self.left)
                return AVLNode.right_rotate(self)

        if balance < -1:
            if AVLNode.get_balance(self.right) <= 0:
                return AVLNode.left_rotate(self)
            else:
                self.right = AVLNode.right_rotate(self.right)
                return AVLNode.left_rotate(self)

        return self


# Driver program to test the above functions
def main():
    root = AVLNode(10)
    keys = [20, 30, 25, 28, 27, -1]

    for key in keys:
        root = root.insert_node(key)
        print("Inserted:", key)
        print("AVL Tree:")
        print(root)

    # Delete
    keys_to_delete = [10, 27]
    for key in keys_to_delete:
        root = root.delete_node(key)
        print("Deleted:", key)
        print("AVL Tree:")
        print(root)


if __name__ == "__main__":
    main()
