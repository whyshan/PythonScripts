import pickle

class syntactic_node:
    def __init__(self, id, syntactic, parent, lexical=''):
        self.id = id
        self.syntactic = syntactic
        self.parent = parent
        self.lexical = lexical
        self.child = []

def generate_tree(elements):
    result = []

    # initial
    elements.reverse()
    upper_level = None
    id = 0

    # generate the tree
    while (len(elements) > 0):
        top = elements.pop()
        if top != '(' and top != ')':
            node = syntactic_node(id, top, upper_level)
            result.append(node)
            id += 1
            upper_level = node
            if elements[-1] != '(' and elements[-1] != ')':
                node.lexical = elements.pop()
        elif top == ')':
            if upper_level != None:
                upper_level = upper_level.parent

    # get children
    for node in result:
        for n in result:
            if n.parent == node:
                node.child.append(n.id)
    return result


filename = "passives_curated.parsed"
tree_original_file = open(filename, "r")
tree_list = []

for eachline in tree_original_file:
    line_with_space = eachline.replace('(', ' ( ').replace(')', ' ) ')
    elements = line_with_space.split()
    tree_list.append(generate_tree(elements))

# print test
for node in tree_list[-1]:
    if (node.parent == None):
        parent = "NULL"
    else:
        parent = node.parent.syntactic
    print "SYN: ", node.syntactic, " | PARENT: ", parent, " | LEX: ", node.lexical, " | ID: ", node.id, " | CHILD: ", node.child

# pickle save
pickle.dump(tree_list, open("syntactic_tree_pickle.txt", "w"))
# pickle read
another_list = pickle.load(open("syntactic_tree_pickle.txt", "r"))