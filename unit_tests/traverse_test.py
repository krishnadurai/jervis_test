''' Unit Test script for traversing functionality in n-ary tree.
'''

import unittest
from tools import captured_output, cook_string_for_list
import sys
import StringIO
from make_tree import make_nary_tree_with_dict
from traverse import bfs
from traverse import dfs
from os import linesep

class TestTraverse(unittest.TestCase):
	''' Test class for traversing functionality in n-ary tree
	'''

	def _boilerplate_test(self, 
			item_list,
			desired_output_bfs_list,
			desired_output_dfs_list):
		''' Common code required to write test function.
			Does the test running mechanism.
		'''
		with captured_output() as (raw_output, error): 
			tree, item_dict = make_nary_tree_with_dict(item_list)
			bfs(tree)
			dfs(tree)
		received_output = raw_output.getvalue().strip()
		test_case_output = cook_string_for_list(desired_output_bfs_list) \
				+ ' ' + linesep + \
				cook_string_for_list(desired_output_dfs_list)
		self.assertEqual(test_case_output.strip(), received_output)

	def test_basic_null(self):
		''' Don't crash when the tree's empty
			IN: None
		'''
		item_list = []
		desired_output_bfs_list = []
		desired_output_dfs_list = []
		self._boilerplate_test(item_list, \
				desired_output_bfs_list, desired_output_dfs_list)

	def test_traverse_on_only_one_node(self):
		''' With only the root node in tree.
			IN: 1
		'''
		item_list = [(None, 1)]
		desired_output_bfs_list = [1]
		desired_output_dfs_list = [1]
		self._boilerplate_test(item_list, \
				desired_output_bfs_list, desired_output_dfs_list)

	def test_traverse_on_simple_node_with_child(self):
		''' Traverse node with a parent having a child already.
			IN:
				1
			   /
			   2
		'''
		item_list = [(None, 1), (1, 2)]
		desired_output_bfs_list = [1, 2]
		desired_output_dfs_list = [2, 1]
		self._boilerplate_test(item_list, \
				desired_output_bfs_list, desired_output_dfs_list)

	def test_traversal_level_movement(self):
		''' Traversal level movement test.
			IN:
				1
			   / \
			   2-3
		'''
		item_list = [(None, 1), (1, 2), (1, 3)]
		desired_output_bfs_list = [1, 2, 3]
		desired_output_dfs_list = [2, 3, 1]
		self._boilerplate_test(item_list, \
				desired_output_bfs_list, desired_output_dfs_list)

	def test_skip_for_start_level_movement(self):
		''' Traversal level movement test when the lower level's
			child is not with the first element of the upper level.
			IN:
				1
			   / \
			   2-3
			      \
				   4
		'''
		item_list = [(None, 1), (1, 2), (1, 3), (3, 4)]
		desired_output_bfs_list = [1, 2, 3, 4]
		desired_output_dfs_list = [4, 2, 3, 1]
		self._boilerplate_test(item_list, \
				desired_output_bfs_list, desired_output_dfs_list)

	def test_sparsed_tree(self):
		''' Test a sparsed tree with randomized nodes.
			IN:
				1
			   / \
			   2-3
			    / \
			   4   5
			  /     \
			 6       7
		'''
		item_list = [(None, 1), (1, 2), (1, 3), (3, 4), (3, 5), (4, 6), (5, 7)]
		desired_output_bfs_list = [1, 2, 3, 4, 5, 6, 7]
		desired_output_dfs_list = [6, 7, 4, 5, 2, 3, 1]
		self._boilerplate_test(item_list, \
				desired_output_bfs_list, desired_output_dfs_list)

if __name__ == '__main__':
	# unittest.main()
	# Let us rather have verbose outputs
	suite = unittest.TestLoader().loadTestsFromTestCase(TestTraverse)
	unittest.TextTestRunner(verbosity=2).run(suite)
