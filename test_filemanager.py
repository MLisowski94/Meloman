import pathlib
import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
import file_managerv2


class TestFileManager(unittest.TestCase):
    def setUp(self) -> None:
        self.testNode = file_managerv2.Node('data')

    def test_node_deafult_init(self):
        '''sprawdzanie czy domyślnym poziomem jest 0, oraz czy
        domyślny rodzic jest pusty'''
        self.assertEqual(0, self.testNode.level)
        self.assertEqual(None, self.testNode.parent)

    def test_node_set_child(self):
        '''Sprawdzanie poprawności funkcji set_child'''
        test_child_node = self.testNode.set_child('data')
        self.assertEqual(self.testNode, test_child_node.get_parent())
        self.assertEqual(1, test_child_node.get_level())
        self.assertIn(test_child_node, self.testNode.children)

    def test_node_is_child(self):
        '''Sprawdzanie poprawności funkcji is_child'''
        first_test_child_node = self.testNode.set_child('data')
        second_test_child_node = first_test_child_node.set_child('data')

        self.assertTrue(first_test_child_node.is_child(self.testNode))
        self.assertTrue(second_test_child_node.is_child(self.testNode))
        self.assertTrue(second_test_child_node.is_child(first_test_child_node))
        self.assertFalse(first_test_child_node.is_child(second_test_child_node))
    def test_add_child(self):
        first_test_node = file_managerv2.Node('data')
        with self.assertRaises(ValueError):
            self.testNode.add_child(first_test_node)
    def test_abandon_parent(self):
        first_test_child_node = self.testNode.set_child('data')
        first_test_child_node.abandon_parent()
        self.assertNotIn(first_test_child_node, self.testNode.children)
        self.assertEqual(first_test_child_node.get_parent(), None)


if __name__ == '__main__':
    unittest.main()
