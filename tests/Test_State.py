import unittest
from State import *
from Edge import *

class TestState(unittest.TestCase):

    def test_constructor_if_assigns_values_properly(self):
        state1 = State(name='A')
        self.assertEqual(state1.state_edges, [])
        self.assertEqual(state1.state_name, 'A')

    def test_constructor_if_assign_edge_properly(self):
        state1 = State(name='A')
        edge1 = Edge(label='a', destination=State('B'))
        self.assertListEqual(state1.state_edges, [])
        state1.add_edge(edge1)
        self.assertEqual(state1.state_edges, [Edge(label='a', destination=State('B'))])


if __name__ == '__main__':
    unittest.main()
