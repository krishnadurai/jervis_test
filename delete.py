''' Module to handle deletion in a n-ary tree
'''

def delete_node(node):
	''' Deletes only a particular node in the n-ary tree.
		Also removes the links which the node has.
	'''
	left_sibling = node.left_sibling
	right_sibling = node.right_sibling
	if left_sibling:
		left_sibling.right_sibling = node.right_sibling
	if right_sibling:
		right_sibling.left_sibling = node.left_sibling
	node.parent_node = None
	node.left_sibling = None
	node.right_sibling = None
	node.left_child = None
	node.right_child = None
	node = None

def delete_range(start_node, end_node):
	''' Deletes a range of nodes in the same level from start_node to end_node.
		Also deletes the nodes' children in a bottom-up fashion.
	'''
	next_node = start_node
	start_node = None
	if end_node:
		end_nodes_right_sibling = end_node.right_sibling
	while next_node and next_node is not end_nodes_right_sibling:
		delete_range(next_node.left_child, next_node.right_child)
		right_sibling = next_node.right_sibling
		delete_node(next_node)
		next_node = right_sibling

def clear_parent_references(node):
	''' Clears parent node's reference to deleted child node if any.
	'''
	parent_node = None
	if node:
		parent_node = node.parent_node
	if parent_node:
		if parent_node.left_child is node and \
				parent_node.right_child is node:
			parent_node.left_child = parent_node.right_child = None
		if parent_node.left_child is node:
			parent_node.left_child = node.right_sibling
		if parent_node.right_child is node:
			parent_node.right_child = node.left_sibling

def delete(node):
	''' Basic deletion function for a n-ary tree.
		Deletes the given node and its children.
		Returns the root of the tree always.
	'''
	tree_root = None
	if node:
		climb_node = node
		while climb_node.parent_node:
			climb_node = climb_node.parent_node
		if climb_node is not node:
			tree_root = climb_node
		clear_parent_references(node)
		delete_range(node, node)
	return tree_root

def debug():
	''' Function for debugging module.
	'''
	from make_tree import make_nary_tree_with_dict, insert
	from traverse import bfs
	from traverse import dfs
	item_list = [(None, 1)]
	tree, item_dict = make_nary_tree_with_dict(item_list)
	insert(tree, 2)
	bfs(tree)
	dfs(tree)
	tree = delete(tree)
	bfs(tree)
	dfs(tree)

if __name__ == '__main__':
	debug()
