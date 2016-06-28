''' Module for traversing a n-ary tree
'''

def bfs(start_node):
	''' Traverses a n-ary tree in a Breadth First manner;
		i.e. Level order traversal.
	'''
	while start_node:
		next_node = start_node
		start_node = None
		while next_node:
			print str(next_node.item),
			if not start_node and next_node.left_child:
				start_node = next_node.left_child
			next_node = next_node.right_sibling
	print ''

def dfs(start_node):
	''' Traverses a n-ary tree in a Depth First manner.
		i.e. Last level in first level printed.
	'''
	stack = []
	while start_node:
		stack.append(start_node)
		next_node = start_node
		start_node = None
		while next_node:
			if next_node.left_child:
				start_node = next_node.left_child
				break # Since only the first node of a level matters
			next_node = next_node.right_sibling
	while stack:
		next_node = stack.pop()
		while next_node:
			print str(next_node.item),
			next_node = next_node.right_sibling
	print ''

