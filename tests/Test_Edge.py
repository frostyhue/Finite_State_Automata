import unittest
from State import *
from Edge import *

class TestEdge(unittest.TestCase):

    def test_constructor_if_assigns_values_properly(self):
        edge1 = Edge(label='a', destination='B')
        self.assertEqual(edge1.edge_label, 'a')
        self.assertEqual(edge1.edge_destination, State('B'))


if __name__ == '__main__':
    unittest.main()
