import unittest
from script5 import Node, Tree      #importuje klasy z poprzedniego skryptu

# - Napisz unit testy (z użyciem pakietu unittest) testujące podstawową funkcjonalność klasy


class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree(1)
        self.tree.add_node(1, 11)
        self.tree.add_node(1, 12)
        self.tree.add_node(11, 111)
        self.tree.add_node(12, 121)
        self.tree.add_node(121, 1221)

    def test_add_node(self):
        self.tree.add_node(12, 122)
        result = self.tree.traverse()
        self.assertIn(122, result)

    def test_traverse(self):
        result = self.tree.traverse()
        expected_result = [1, 11, 111, 12, 121, 1221]
        self.assertEqual(result, expected_result)

    def test_str(self):
        expected_str = (
            "1\n"
            "\t11\n"
            "\t\t111\n"
            "\t12\n"
            "\t\t121\n"
            "\t\t\t1221\n"
        )
        self.assertEqual(str(self.tree), expected_str)

    def test_find_node(self):
        node = self.tree.find_node(111)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 111)

        node = self.tree.find_node(3)
        self.assertIsNone(node)


if __name__ == "__main__":
    unittest.main()