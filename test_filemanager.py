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

    def test_node_add_child(self):
        pass

    def test_node_is_ancestor(self):
        pass



if __name__ == '__main__':
    unittest.main()
