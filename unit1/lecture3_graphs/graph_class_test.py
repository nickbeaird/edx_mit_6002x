import unittest
from graph_class import Node, Edge

class TestNodeClass(unittest.TestCase):
    """Test Node and Edge class assumption

    Attempt to use UnitTest TestCase to highlight the functionality needed
    in the corresponding files.
    """

    def setUp(self):
        self.node1 = Node('node_one')
        self.node2 = Node('node_two')
        self.edge = Edge(self.node1, self.node2)

    def test_node(self):
        self.assertEqual(self.node1.getName(), 'node_one')
        self.assertEqual(self.node2.getName(), 'node_two')
        self.assertIsNot(self.node1.getName(), self.node2.getName())

    def test_edge_str_returns_node_names(self):
        expected_result = self.node1.getName() + ' ->' + self.node2.getName()
        self.assertEqual(self.edge.__str__(), expected_result)
        
if __name__ == "__main__":
    """Note that this is not fully tested classes. This is for informational and skill
    building purposes only."""
    unittest.main()