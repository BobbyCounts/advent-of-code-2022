tree_array = []
def trees_vis(tree_list, tree_height):
	tree_seen = 0
	for tree in tree_list:
		if tree < tree_height:
			tree_seen += 1
			continue
		else:
			tree_seen += 1
			return tree_seen
	return tree_seen 

with open("input.txt", "r") as input_file:
	for line in input_file:
		if line == '\n':
			break
		#remove newline
		line = line[0:-1]
		temp = []
		for number in line:
			temp.append(int(number))
		tree_array.append(temp)

visible_trees = 0
scenic_score = []

last_row = len(tree_array) - 1
last_col = len(tree_array[0]) - 1

for i in range(len(tree_array)):
	for j in range(len(tree_array[0])):
		#outside perimeter
		if(i == 0 or j == 0 or i == last_row or j == last_col):
			visible_trees += 1
			continue
		
		#create list of trees in each direction
		right = tree_array[i][j+1:]	
		left = tree_array[i][0:j]
		col = [row[j] for row in tree_array]
		up = col[0:i]
		down = col[i+1:]
		
		smallest_tree = min([max(left), max(right), max(up), max(down)])
		
		current_h = tree_array[i][j]
		
		left.reverse()
		up.reverse()
		
		seen_trees = [trees_vis(left,current_h), trees_vis(right,current_h), trees_vis(up,current_h), trees_vis(down,current_h)]
		score = seen_trees[0] * seen_trees[1] * seen_trees[2] * seen_trees[3]
		scenic_score.append(score)
		
		if smallest_tree < current_h:
			visible_trees += 1

print(visible_trees)	
print(max(scenic_score))
