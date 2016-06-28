''' Unit Test script for delete functionality in n-ary tree.
'''

import unittest
from tools import captured_output, cook_string_for_list
import sys
import StringIO
from make_tree import make_nary_tree_with_dict
from delete import delete
from traverse import bfs
from traverse import dfs
from os import linesep

class TestDelete(unittest.TestCase):
	''' Test class for delete functionality in n-ary tree
	'''
	
	def _boilerplate_test(self, 
			item_list,
			to_be_deleted_item,
			desired_input_bfs_list,
			desired_input_dfs_list,
			desired_output_bfs_list,
			desired_output_dfs_list):
		''' Common code required to write test function.
			Does the test running mechanism.
		'''
		with captured_output() as (raw_output, error): 
			tree, item_dict = make_nary_tree_with_dict(item_list)
			bfs(tree)
			dfs(tree)
			if to_be_deleted_item is not None:
				tree = delete(item_dict[to_be_deleted_item])
			else:
				tree = delete(None)
			bfs(tree)
			dfs(tree)
		received_output = raw_output.getvalue().strip()
		test_case_output = cook_string_for_list(desired_input_bfs_list) \
				+ ' ' + linesep + \
				cook_string_for_list(desired_input_dfs_list) \
				+ ' ' + linesep + \
				cook_string_for_list(desired_output_bfs_list) \
				+ ' ' + linesep + \
				cook_string_for_list(desired_output_dfs_list)
		self.assertEqual(test_case_output.strip(), received_output)

	def test_basic_null(self):
		''' Don't crash when the tree's empty
			IN: None
			OUT: None
		'''
		item_list = []
		to_be_deleted_item = None
		desired_input_bfs_list = []
		desired_input_dfs_list = []
		desired_output_bfs_list = []
		desired_output_dfs_list = []
		self._boilerplate_test(item_list, to_be_deleted_item, \
				desired_input_bfs_list, desired_input_dfs_list, \
				desired_output_bfs_list, desired_output_dfs_list)

	def test_delete_on_only_one_node(self):
		''' Delete with only the root node in tree.
			IN: 1
			OUT: None 
		'''
		item_list = [(None, 1)]
		to_be_deleted_item = 1
		desired_input_bfs_list = [1]
		desired_input_dfs_list = [1]
		desired_output_bfs_list = []
		desired_output_dfs_list = []
		self._boilerplate_test(item_list, to_be_deleted_item, \
				desired_input_bfs_list, desired_input_dfs_list, \
				desired_output_bfs_list, desired_output_dfs_list)

	def test_delete_in_basic_single_node_next_level(self):
		''' Delete a simple node in next level
			IN:
				1
			   / \
			   2-3
			OUT: 
				1
			   /
			   2
		'''
		item_list = [(None, 1), (1, 2), (1, 3)]
		to_be_deleted_item = 3
		desired_input_bfs_list = [1, 2, 3]
		desired_input_dfs_list = [2, 3, 1]
		desired_output_bfs_list = [1, 2]
		desired_output_dfs_list = [2, 1]
		self._boilerplate_test(item_list, to_be_deleted_item, \
				desired_input_bfs_list, desired_input_dfs_list, \
				desired_output_bfs_list, desired_output_dfs_list)

	def test_delete_with_siblings_on_both_sides(self):
		''' Delete a node with siblings on both sides.
			IN:
				1
			   / \
			   2-3
			  / \ \
		     4 - 5-6
			OUT: 
				1
			   / \
			   2-3
			  /   \
		     4	   6
		'''
		item_list = [(None, 1), (1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
		to_be_deleted_item = 5
		desired_input_bfs_list = [1, 2, 3, 4, 5, 6]
		desired_input_dfs_list = [4, 5, 6, 2, 3, 1]
		desired_output_bfs_list = [1, 2, 3, 4, 6]
		desired_output_dfs_list = [4, 6, 2, 3, 1]
		self._boilerplate_test(item_list, to_be_deleted_item, \
				desired_input_bfs_list, desired_input_dfs_list, \
				desired_output_bfs_list, desired_output_dfs_list)

	def test_delete_on_multi_levels(self):
		''' Delete a node with multilevel children.
			IN:
				1
			   / \
			   2-3
			  / \ \
		     4 - 5-6
			 /\ /   \
			7 8 9   10
			OUT: 
				1
			     \
			     3
			      \
		      	   6
				    \
					10
		'''
		item_list = [(None, 1), (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), \
				(4, 7), (4, 8), (5, 9), (6, 10)]
		to_be_deleted_item = 2
		desired_input_bfs_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		desired_input_dfs_list = [7, 8, 9, 10, 4, 5, 6, 2, 3, 1]
		desired_output_bfs_list = [1, 3, 6, 10]
		desired_output_dfs_list = [10, 6, 3, 1]
		self._boilerplate_test(item_list, to_be_deleted_item, \
				desired_input_bfs_list, desired_input_dfs_list, \
				desired_output_bfs_list, desired_output_dfs_list)

	def test_delete_far_right(self):
		''' Delete a node with far sibling on left side.
			IN:
				1
			   / \
			   2-3
			  / \ \
		     4 - 5-6
			 /      \
			7        8
			OUT: 
				1
			   / \
			   2-3
			  / \ \
		     4 - 5-6
			 / 
			7
		'''
		item_list = [(None, 1), (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), \
				(4, 7), (6, 8)]
		to_be_deleted_item = 8
		desired_input_bfs_list = [1, 2, 3, 4, 5, 6, 7, 8]
		desired_input_dfs_list = [7, 8, 4, 5, 6, 2, 3, 1]
		desired_output_bfs_list = [1, 2, 3, 4, 5, 6, 7]
		desired_output_dfs_list = [7, 4, 5, 6, 2, 3, 1]
		self._boilerplate_test(item_list, to_be_deleted_item, \
				desired_input_bfs_list, desired_input_dfs_list, \
				desired_output_bfs_list, desired_output_dfs_list)

	def test_delete_far_left(self):
		''' Delete a node with far sibling on left side.
			IN:
				1
			   / \
			   2-3
			  / \ \
		     4 - 5-6
			 /      \
			7        8
			OUT: 
				1
			   / \
			   2-3
			  / \ \
		     4 - 5-6
			        \
			         8
		'''
		item_list = [(None, 1), (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), \
				(4, 7), (6, 8)]
		to_be_deleted_item = 7
		desired_input_bfs_list = [1, 2, 3, 4, 5, 6, 7, 8]
		desired_input_dfs_list = [7, 8, 4, 5, 6, 2, 3, 1]
		desired_output_bfs_list = [1, 2, 3, 4, 5, 6, 8]
		desired_output_dfs_list = [8, 4, 5, 6, 2, 3, 1]
		self._boilerplate_test(item_list, to_be_deleted_item, \
				desired_input_bfs_list, desired_input_dfs_list, \
				desired_output_bfs_list, desired_output_dfs_list)

	def test_delete_on_multi_levels_variation(self):
		''' Delete a node with multilevel children.
				1
			     \
			     3
			      \
		      	   6
				    \
					10
		'''
		item_list = [(None, 1), (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), \
				(4, 7), (4, 8), (5, 9), (6, 10)]
		to_be_deleted_item = 2
		desired_input_bfs_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		desired_input_dfs_list = [7, 8, 9, 10, 4, 5, 6, 2, 3, 1]
		desired_output_bfs_list = [1, 3, 6, 10]
		desired_output_dfs_list = [10, 6, 3, 1]
		self._boilerplate_test(item_list, to_be_deleted_item, \
				desired_input_bfs_list, desired_input_dfs_list, \
				desired_output_bfs_list, desired_output_dfs_list)

	def test_delete_on_multi_levels_variation(self):
		''' Delete a node with multilevel children.
			IN:
				1
			   / \
			   2-3
			  / \ \
		     4 - 5-6
			 /\ /   \
			7 8 9   10
			OUT: 
				1
			   /
			   2
			  / \
		     4 - 5
			 /\ /
			7 8 9
		'''
		item_list = [(None, 1), (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), \
				(4, 7), (4, 8), (5, 9), (6, 10)]
		to_be_deleted_item = 3
		desired_input_bfs_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		desired_input_dfs_list = [7, 8, 9, 10, 4, 5, 6, 2, 3, 1]
		desired_output_bfs_list = [1, 2, 4, 5, 7, 8, 9]
		desired_output_dfs_list = [7, 8, 9, 4, 5, 2, 1]
		self._boilerplate_test(item_list, to_be_deleted_item, \
				desired_input_bfs_list, desired_input_dfs_list, \
				desired_output_bfs_list, desired_output_dfs_list)

	def test_delete_on_multi_level_middle_value(self):
		''' Delete a node with multilevel children.
			IN:
				1
			   / \
			   2-3
			  / \ \
		     4 - 5-6
			 /\ /   \
			7 8 9   10
			OUT: 
				1
			   / \
			   2-3
			  /   \
		     4     6
			 /\     \
			7 8     10
		'''
		item_list = [(None, 1), (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), \
				(4, 7), (4, 8), (5, 9), (6, 10)]
		to_be_deleted_item = 5
		desired_input_bfs_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		desired_input_dfs_list = [7, 8, 9, 10, 4, 5, 6, 2, 3, 1]
		desired_output_bfs_list = [1, 2, 3, 4, 6, 7, 8, 10]
		desired_output_dfs_list = [7, 8, 10, 4, 6, 2, 3, 1]
		self._boilerplate_test(item_list, to_be_deleted_item, \
				desired_input_bfs_list, desired_input_dfs_list, \
				desired_output_bfs_list, desired_output_dfs_list)

if __name__ == '__main__':
	# unittest.main()
	# Let us rather have verbose outputs
	suite = unittest.TestLoader().loadTestsFromTestCase(TestDelete)
	unittest.TextTestRunner(verbosity=2).run(suite)
