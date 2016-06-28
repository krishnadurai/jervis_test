''' Module to create and insert in a nary tree.
'''

class Node(object):
	''' Basic node of a n-ary tree.
	'''
	def __init__(self, parent_node, item):
		self.parent_node = parent_node
		self.item = item
		self.left_sibling = None
		self.right_sibling = None
		self.left_child = None
		self.right_child = None

def make_nary_tree_with_dict(item_list):
	''' Converts a list of tuples containing (tree node parent, item)
		to a n-ary tree.
		The first entry in the item_list should have 'None' as tree node
		parent, as it is the root.
		Also returns a maping of created nodes with their item as keys
		in a dictionary.
		Used for unit testing.
	'''
	tree_root = None
	item_dict = dict()
	for item in item_list:
		parent_item, child_item = item
		if not tree_root:
			tree_root = insert(None, child_item) # None as it is the root
			item_dict[child_item] = tree_root
		else:
			new_node = insert(item_dict[parent_item], child_item)
			assert item_dict.get(child_item) == None
			item_dict[child_item] = new_node
	return tree_root, item_dict

def get_left_sibling(node):
	''' Gets a left sibling to a node if found or None
	'''
	parent = node.parent_node
	if parent:
		if parent.right_child:
			return parent.right_child
		left_aunt = parent.left_sibling 
		while left_aunt:
			if left_aunt.right_child:
				return left_aunt.right_child
			left_aunt = left_aunt.left_sibling
	return None

def get_right_sibling(node):
	''' Gets a right sibling to a node only when it is not acquired from
		the left sibling's right link.
		i.e. It finds it from the right aunt if found or None
	'''
	parent = node.parent_node
	if parent:
		right_aunt = parent.right_sibling 
		while right_aunt:
			if right_aunt.left_child:
				return right_aunt.left_child
			right_aunt = right_aunt.right_sibling
	return None

def insert(parent_node, item):
	''' Inserts an item by creating a node and as the rightmost child of
		the parent_node.
	'''
	assert item is not None
	new_node = Node(parent_node, item)
	left_sibling = get_left_sibling(new_node)
	right_sibling = None
	if left_sibling:
		right_sibling = left_sibling.right_sibling
		left_sibling.right_sibling = new_node
		new_node.left_sibling = left_sibling
	if not right_sibling:
		right_sibling = get_right_sibling(new_node)
	if right_sibling:
		right_sibling.left_sibling = new_node
		new_node.right_sibling = right_sibling
	if parent_node:
		parent_node.right_child = new_node
		if not parent_node.left_child:
			parent_node.left_child = new_node
	return new_node

def debug():
	''' Function for debugging module.
	'''
	from traverse import bfs
	from traverse import dfs
	item_list = [(None, 1)]
	tree, item_dict = make_nary_tree_with_dict(item_list)
	insert(tree, 2)
	bfs(tree)
	dfs(tree)

if __name__ == '__main__':
	debug()
