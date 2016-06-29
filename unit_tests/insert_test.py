''' Unit Test script for insert functionality in n-ary tree.
'''

import unittest
from tools import captured_output, cook_string_for_list
import sys
import StringIO
from make_tree import make_nary_tree_with_dict, insert
from traverse import bfs
from traverse import dfs
from os import linesep

class TestInsert(unittest.TestCase):
	''' Test class for insert functionality in n-ary tree
	'''

	def _boilerplate_test(self, 
			item_list,
			parent_of_new_item,
			to_be_inserted_item,
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
			if parent_of_new_item is not None:
				insert(item_dict[parent_of_new_item], to_be_inserted_item)
			else:
				tree = insert(None, to_be_inserted_item)
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
			OUT:
				1
		'''
		item_list = []
		parent_of_new_node = None
		to_be_inserted_item = 1
		desired_input_bfs_list = []
		desired_input_dfs_list = []
		desired_output_bfs_list = [1]
		desired_output_dfs_list = [1]
		self._boilerplate_test(item_list, parent_of_new_node, \
				to_be_inserted_item, desired_input_bfs_list, \
				desired_input_dfs_list, desired_output_bfs_list, \
				desired_output_dfs_list)

	def test_insert_on_only_one_parent(self):
		''' Insert with only the root node in tree.
			IN: 1
			OUT: 
				1
			   /
			   2
		'''
		item_list = [(None, 1)]
		parent_of_new_node = 1
		to_be_inserted_item = 2
		desired_input_bfs_list = [1]
		desired_input_dfs_list = [1]
		desired_output_bfs_list = [1, 2]
		desired_output_dfs_list = [2, 1]
		self._boilerplate_test(item_list, parent_of_new_node, \
				to_be_inserted_item, desired_input_bfs_list, \
				desired_input_dfs_list, desired_output_bfs_list, \
				desired_output_dfs_list)
	
	def test_insert_in_simple_node_with_child(self):
		''' Insert a new node with a parent having a child already.
			IN:
				1
			   /
			   2
			OUT: 
				1
			   / \
			   2-3
		'''
		item_list = [(None, 1), (1, 2)]
		parent_of_new_node = 1
		to_be_inserted_item = 3
		desired_input_bfs_list = [1, 2]
		desired_input_dfs_list = [2, 1]
		desired_output_bfs_list = [1, 2, 3]
		desired_output_dfs_list = [2, 3, 1]
		self._boilerplate_test(item_list, parent_of_new_node, \
				to_be_inserted_item, desired_input_bfs_list, \
				desired_input_dfs_list, desired_output_bfs_list, \
				desired_output_dfs_list)

	def test_insert_new_on_level(self):
		''' Insert a new node in a new level.
			IN:
				1
			   / \
			   2-3
			OUT: 
				1
			   / \
			   2-3
			      \
				   4
		'''
		item_list = [(None, 1), (1, 2), (1, 3)]
		parent_of_new_node = 3
		to_be_inserted_item = 4
		desired_input_bfs_list = [1, 2, 3]
		desired_input_dfs_list = [2, 3, 1]
		desired_output_bfs_list = [1, 2, 3, 4]
		desired_output_dfs_list = [4, 2, 3, 1]
		self._boilerplate_test(item_list, parent_of_new_node, \
				to_be_inserted_item, desired_input_bfs_list, \
				desired_input_dfs_list, desired_output_bfs_list, \
				desired_output_dfs_list)

	def test_insert_leftmost_with_right_sibling(self):
		''' Insert a new node as leftmost node in a level.
			IN:
				1
			   / \
			   2-3
			      \
				   4
			OUT: 
				1
			   / \
			   2-3
			  /   \
		     5	   4
		'''
		item_list = [(None, 1), (1, 2), (1, 3), (3, 4)]
		parent_of_new_node = 2
		to_be_inserted_item = 5
		desired_input_bfs_list = [1, 2, 3, 4]
		desired_input_dfs_list = [4, 2, 3, 1]
		desired_output_bfs_list = [1, 2, 3, 5, 4]
		desired_output_dfs_list = [5, 4, 2, 3, 1]
		self._boilerplate_test(item_list, parent_of_new_node, \
				to_be_inserted_item, desired_input_bfs_list, \
				desired_input_dfs_list, desired_output_bfs_list, \
				desired_output_dfs_list)

	def test_insert_rightmost_with_left_sibling(self):
		''' Insert a new node as rightmost node in a level.
			IN:
				1
			   / \
			   2-3
			  / 
		     4
			OUT: 
				1
			   / \
			   2-3
			  /   \
		     4	   5
		'''
		item_list = [(None, 1), (1, 2), (1, 3), (2, 4)]
		parent_of_new_node = 3
		to_be_inserted_item = 5
		desired_input_bfs_list = [1, 2, 3, 4]
		desired_input_dfs_list = [4, 2, 3, 1]
		desired_output_bfs_list = [1, 2, 3, 4, 5]
		desired_output_dfs_list = [4, 5, 2, 3, 1]
		self._boilerplate_test(item_list, parent_of_new_node, \
				to_be_inserted_item, desired_input_bfs_list, \
				desired_input_dfs_list, desired_output_bfs_list, \
				desired_output_dfs_list)

	def test_insert_with_siblings_on_both_sides(self):
		''' Insert a new node with siblings on both sides.
			IN:
				1
			   / \
			   2-3
			  /   \
		     4	   5
			OUT: 
				1
			   / \
			   2-3
			  / \ \
		     4 - 6-5
		'''
		item_list = [(None, 1), (1, 2), (1, 3), (2, 4), (3, 5)]
		parent_of_new_node = 2
		to_be_inserted_item = 6
		desired_input_bfs_list = [1, 2, 3, 4, 5]
		desired_input_dfs_list = [4, 5, 2, 3, 1]
		desired_output_bfs_list = [1, 2, 3, 4, 6, 5]
		desired_output_dfs_list = [4, 6, 5, 2, 3, 1]
		self._boilerplate_test(item_list, parent_of_new_node, \
				to_be_inserted_item, desired_input_bfs_list, \
				desired_input_dfs_list, desired_output_bfs_list, \
				desired_output_dfs_list)

	def test_far_insert_right(self):
		''' Insert a new node with far sibling on left side
			IN:
				 1
			   / \ \
			   2-3-4
			  /
		     5  
			OUT: 
				 1
			   / \ \
			   2-3-4
			  /     \
		     5       6
		'''
		item_list = [(None, 1), (1, 2), (1, 3), (1, 4), (2, 5)]
		parent_of_new_node = 4
		to_be_inserted_item = 6
		desired_input_bfs_list = [1, 2, 3, 4, 5]
		desired_input_dfs_list = [5, 2, 3, 4, 1]
		desired_output_bfs_list = [1, 2, 3, 4, 5, 6]
		desired_output_dfs_list = [5, 6, 2, 3, 4, 1]
		self._boilerplate_test(item_list, parent_of_new_node, \
				to_be_inserted_item, desired_input_bfs_list, \
				desired_input_dfs_list, desired_output_bfs_list, \
				desired_output_dfs_list)

	def test_far_insert_left(self):
		''' Insert a new node with far sibling on right side
			IN:
				 1
			   / \ \
			   2-3-4
			        \
		            5 
			OUT: 
				 1
			   / \ \
			   2-3-4
			  /     \
		     6       5
		'''
		item_list = [(None, 1), (1, 2), (1, 3), (1, 4), (4, 5)]
		parent_of_new_node = 2
		to_be_inserted_item = 6
		desired_input_bfs_list = [1, 2, 3, 4, 5]
		desired_input_dfs_list = [5, 2, 3, 4, 1]
		desired_output_bfs_list = [1, 2, 3, 4, 6, 5]
		desired_output_dfs_list = [6, 5, 2, 3, 4, 1]
		self._boilerplate_test(item_list, parent_of_new_node, \
				to_be_inserted_item, desired_input_bfs_list, \
				desired_input_dfs_list, desired_output_bfs_list, \
				desired_output_dfs_list)

	def test_far_insert_from_both_sides(self):
		''' Insert a new node with far sibling on both sides
			IN:
				   1
			   / / | \ \
			  2-3- 4-5-6
			 /         \
		     7          8
			OUT: 
				   1
			   / / | \ \
			  2-3- 4-5-6
			 /     |   \
		     7     9    8
		'''
		item_list = [(None, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), \
				(2, 7), (6, 8)]
		parent_of_new_node = 4
		to_be_inserted_item = 9
		desired_input_bfs_list = [1, 2, 3, 4, 5, 6, 7, 8]
		desired_input_dfs_list = [7, 8, 2, 3, 4, 5, 6, 1]
		desired_output_bfs_list = [1, 2, 3, 4, 5, 6, 7, 9, 8]
		desired_output_dfs_list = [7, 9, 8, 2, 3, 4, 5, 6, 1]
		self._boilerplate_test(item_list, parent_of_new_node, \
				to_be_inserted_item, desired_input_bfs_list, \
				desired_input_dfs_list, desired_output_bfs_list, \
				desired_output_dfs_list)

if __name__ == '__main__':
	# unittest.main()
	# Let us rather have verbose outputs
	suite = unittest.TestLoader().loadTestsFromTestCase(TestInsert)
	unittest.TextTestRunner(verbosity=2).run(suite)
