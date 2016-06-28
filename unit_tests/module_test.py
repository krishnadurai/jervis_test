''' Module Test script for testing all functionality in tandem in n-ary tree.
'''

import unittest
from tools import captured_output, cook_string_for_list
import sys
import StringIO
from make_tree import insert
from delete import delete
from traverse import bfs
from traverse import dfs
from os import linesep

class TestModule(unittest.TestCase):
	''' Test class for n-ary tree module.
	'''

	def _test_operation_insert(self,
			tree,
			parent_of_new_item,
			item,
			item_dict,
			desired_output_bfs_list,
			desired_output_dfs_list):
		''' Performs insert operation and also checks
			for its correctness.
		'''
		items_node = None
		with captured_output() as (raw_output, error): 
			if parent_of_new_item is not None:
				items_node = insert(item_dict[parent_of_new_item], item)
			else:
				items_node = insert(None, item)
				tree = items_node
			item_dict[item] = items_node
			bfs(tree)
			dfs(tree)
		received_output = raw_output.getvalue().strip()
		test_case_output = cook_string_for_list(desired_output_bfs_list) \
				+ ' ' + linesep + \
				cook_string_for_list(desired_output_dfs_list)
		self.assertEqual(test_case_output.strip(), received_output)
		return tree

	def _test_operation_delete(self,
			item,
			item_dict,
			desired_output_bfs_list,
			desired_output_dfs_list):
		''' Performs delete operation and also checks
			for its correctness.
		'''
		tree = None
		with captured_output() as (raw_output, error): 
			if item is not None:
				tree = delete(item_dict[item])
				del item_dict[item]
			else:
				tree = delete(None)
			bfs(tree)
			dfs(tree)
		received_output = raw_output.getvalue().strip()
		test_case_output = cook_string_for_list(desired_output_bfs_list) \
				+ ' ' + linesep + \
				cook_string_for_list(desired_output_dfs_list)
		self.assertEqual(test_case_output.strip(), received_output)
		return tree
	
	def test_basic_tree(self):
		''' Simulates tree operations for checking correctness.
		'''
		tree = None
		item_dict = {}
		
		# Initialize tree.
		desired_output_bfs_list = [1]
		desired_output_dfs_list = [1]
		tree = self._test_operation_insert(tree, None, 1, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

		desired_output_bfs_list = []
		desired_output_dfs_list = []
		tree = self._test_operation_delete(1, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

	def test_tree(self):
		''' Simulates tree operations for checking correctness.
		'''
		tree = None
		item_dict = {}
		
		# Step 1: Initialize tree.
		desired_output_bfs_list = [1]
		desired_output_dfs_list = [1]
		tree = self._test_operation_insert(tree, None, 1, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)
		
		# Step 2:
		desired_output_bfs_list = [1, 2]
		desired_output_dfs_list = [2, 1]
		self._test_operation_insert(tree, 1, 2, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)
		
		# Step 3:
		desired_output_bfs_list = [1, 2, 3]
		desired_output_dfs_list = [2, 3, 1]
		self._test_operation_insert(tree, 1, 3, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

		# Step 4:
		desired_output_bfs_list = [1, 2]
		desired_output_dfs_list = [2, 1]
		tree = self._test_operation_delete(3, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

		# Step 5:
		desired_output_bfs_list = [1, 2, 3]
		desired_output_dfs_list = [3, 2, 1]
		self._test_operation_insert(tree, 2, 3, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

		# Step 6:
		desired_output_bfs_list = [1, 2, 4, 3]
		desired_output_dfs_list = [3, 2, 4, 1]
		self._test_operation_insert(tree, 1, 4, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

		# Step 7:
		desired_output_bfs_list = [1, 2, 4, 5, 3]
		desired_output_dfs_list = [3, 2, 4, 5, 1]
		self._test_operation_insert(tree, 1, 5, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

		# Step 8:
		desired_output_bfs_list = [1, 2, 4, 5, 3, 6]
		desired_output_dfs_list = [3, 6, 2, 4, 5, 1]
		self._test_operation_insert(tree, 2, 6, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

		# Step 9:
		desired_output_bfs_list = [1, 2, 4, 5, 3, 6, 7]
		desired_output_dfs_list = [3, 6, 7, 2, 4, 5, 1]
		self._test_operation_insert(tree, 5, 7, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

		# Step 10:
		desired_output_bfs_list = [1, 2, 4, 5, 6, 7]
		desired_output_dfs_list = [6, 7, 2, 4, 5, 1]
		tree = self._test_operation_delete(3, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

		# Step 11:
		desired_output_bfs_list = [1, 2, 4, 5, 7]
		desired_output_dfs_list = [7, 2, 4, 5, 1]
		tree = self._test_operation_delete(6, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

		# Step 12:
		desired_output_bfs_list = [1, 2, 4, 5, 3, 7]
		desired_output_dfs_list = [3, 7, 2, 4, 5, 1]
		self._test_operation_insert(tree, 2, 3, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

		# Step 13:
		desired_output_bfs_list = [1, 2, 4, 5, 3]
		desired_output_dfs_list = [3, 2, 4, 5, 1]
		tree = self._test_operation_delete(7, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

		# Step 14:
		desired_output_bfs_list = [1, 2, 4, 5, 3, 6]
		desired_output_dfs_list = [3, 6, 2, 4, 5, 1]
		self._test_operation_insert(tree, 5, 6, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

		# Step 15:
		desired_output_bfs_list = [1, 2, 4, 5, 3, 7, 6]
		desired_output_dfs_list = [3, 7, 6, 2, 4, 5, 1]
		self._test_operation_insert(tree, 4, 7, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

		# Step 16:
		desired_output_bfs_list = [1, 2, 4, 3, 7]
		desired_output_dfs_list = [3, 7, 2, 4, 1]
		tree = self._test_operation_delete(5, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

		# Step 17:
		desired_output_bfs_list = []
		desired_output_dfs_list = []
		tree = self._test_operation_delete(1, item_dict, 
				desired_output_bfs_list, desired_output_dfs_list)

if __name__ == '__main__':
	# unittest.main()
	# Let us rather have verbose outputs
	suite = unittest.TestLoader().loadTestsFromTestCase(TestModule)
	unittest.TextTestRunner(verbosity=2).run(suite)
