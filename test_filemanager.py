import pathlib
import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
import file_managerv2
import node
import file


class TestNode(unittest.TestCase):
    def setUp(self) -> None:
        self.testNode = node.Node('data', 'title')

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
        self.assertIn(test_child_node, self.testNode.children_list)
        self.assertEqual(self.testNode.title, test_child_node.title)

    def test_node_set_child_with_diferent_data_type(self):
        with self.assertRaises(TypeError):
            test_child_node = self.testNode.set_child(1)


    def test_node_is_child_of(self):
        '''Sprawdzanie poprawności funkcji is_child'''
        first_test_child_node = self.testNode.set_child('data')
        second_test_child_node = first_test_child_node.set_child('data')

        self.assertTrue(first_test_child_node.is_child_of(self.testNode))
        self.assertTrue(second_test_child_node.is_child_of(self.testNode))
        self.assertTrue(second_test_child_node.is_child_of(first_test_child_node))
        self.assertFalse(first_test_child_node.is_child_of(second_test_child_node))

    # def test_add_child(self):
    #     first_test_node = file_managerv2.Node('data')
    #     with self.assertRaises(ValueError):
    #         self.testNode.add_child(first_test_node)
    def test_abandon_parent(self):
        first_test_child_node = self.testNode.set_child('data')
        first_test_child_node.abandon_parent()
        self.assertNotIn(first_test_child_node, self.testNode.children_list)
        self.assertEqual(first_test_child_node.get_parent(), None)
class TestFile(unittest.TestCase):
    '''
    Testy sprawdzające czy podczas inicializacji obiektu wyrzucane są wyjątki
    dotyczące nieprawidłowego typu adresu i adresu nie istniejącego
    '''
    def test_file_init_type_check(self):
        with self.assertRaises(TypeError):
            test_file = file.File('x', 'y')
    def test_file_init_exist_check(self):
        with self.assertRaises(ValueError):
            test_file = file.File('x', Path('x'))

if __name__ == '__main__':
    unittest.main()
