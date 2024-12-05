# - Zaimplementuj klasę, która będzie realizowała strukturę drzewa (powinna posiada
#  funkcję przechodzenia wszystkich węzłów drzewa, węzły powinny mie
#  możliwość przechowywania wartości, krawędzie także mogą zawiera
#  wartości lub by
#  oznaczone), klasa powinna mie
#  zdefiniowaną funkcję __str__


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __str__(self):
        return str(self.value)

    def add_child(self, child_value):
        self.children.append(Node(child_value))

    def find(self, value):  # funkcja rekurencyjna zwracająca węzeł z szukaną wartością
        if self.value == value:
            return self
        for node in self.children:
            found_value = node.find(value)
            if found_value:
                return found_value
        return None


class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def find_node(self, value):
        found_node = self.root.find(value)  # -
        if found_node:
            return found_node
        return None

    def add_node(self, parent_value, child_value):
        parent_node = self.find_node(parent_value)
        if parent_node:
            parent_node.add_child(child_value)

    def traverse(self, node=None):
        if node is None:
            node = self.root
        result = []
        result.append(node.value)
        for child in node.children:
            result.extend(self.traverse(child))
        return result

    def __str__(self):
        def build_tree_string(node, prefix=""):
            result = f"{prefix}{node.value}\n"
            for child in node.children:
                result += build_tree_string(child, prefix + "\t")
            return result

        return build_tree_string(self.root)


if __name__ == "__main__":
    tree = Tree(1)
    tree.add_node(1, 11)
    tree.add_node(1, 12)
    tree.add_node(11, 111)
    tree.add_node(12, 121)
    tree.add_node(12, 122)
    tree.add_node(122, 1221)
    #print(tree.traverse())
    print(tree)