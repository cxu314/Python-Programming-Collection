class TrieNode:
    """A class of nodes in a TrieTree.

    Attributes:
        char: The character of the node.
        parent: The parent of the node.
        children: The children of the node.
        is_leaf: Whether the node is leaf or not.
                 If it is lead, then the characters of
                 all nodes from the root to this node
                 could consist a word.
    """

    def __init__(self, char, parent):
        self.char = char
        self.parent = parent
        self.children = {}
        self.is_leaf = False

    def add_child(self, child_node):
        """
        This function adds a child node to the current node.
        """
        self.children[child_node.char] = child_node


class TrieTree:
    """A TrieTree construced by a given list of words.

    Attributes:
        root: The root of TrieTree.
    """

    def __init__(self, words):
        self.root = TrieNode(None, None)

        for idx, word in enumerate(words):
            node = self.root
            for x in range(len(word)):
                try:
                    node = node.children[word[x]]
                except KeyError:
                    node.add_child(TrieNode(word[x], node))
                    node = node.children[word[x]]
            node.is_leaf = True


def clean_phone_number(phone_number):
    """
    This function takes a string of phone number and
    returns a list of valid numbers from 2 to 9.
    """
    valid_numbers = set(['2', '3', '4', '5', '6', '7', '8', '9'])
    return [x for x in list(phone_number) if x in valid_numbers]


def telephone_keypad_words(phone_number, tree, keypad_dict):
    """
    This function takes a string of phone number,
    a TrieTree construced by a given list of words,
    and a dictionary mapping numbers to characters on a telephone keypad
    and returns a sorted list of all possible words.
    """
    from queue import Queue

    cleaned_phone_number = clean_phone_number(phone_number)

    parent_nodes = Queue()
    child_nodes = Queue()
    parent_nodes.put(tree.root)

    for n in cleaned_phone_number:
        while not parent_nodes.empty():
            current_parent_node = parent_nodes.get()
            for char in keypad_dict[n]:
                try:
                    child_nodes.put(current_parent_node.children[char])
                except KeyError:
                    pass

        while not child_nodes.empty():
            parent_nodes.put(child_nodes.get())

    while not parent_nodes.empty():
        node = parent_nodes.get()
        if node.is_leaf:
            node_string = []
            while node.char is not None:
                node_string.append(node.char)
                node = node.parent
            print(''.join(reversed(node_string)))


if __name__ == "__main__":
    import sys

    keypad_dict = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}

    phone_number = sys.argv[1]
    words = [w.strip() for w in sys.stdin.readlines()]
    tree = TrieTree(words)

    telephone_keypad_words(phone_number, tree, keypad_dict)
