import queue
import random


class Node:
    """A class of node in Graph.

    Argument:
      node_dict: A dictionary with a name of the node as a key
                 and a list of nodes it is connected to as value.
                 For example, Node({'A':['B','C']}).
                 Empty list is a legal dictionary value,
                 such as Node({'A':[]}).
                 Any other input to the node should result in an error.

    Attributes:
        dict: A dictionary with a name of the node as a key
              and a list of nodes it is connected to as value.
    """
    def __init__(self, node_dict):
        if isinstance(node_dict, dict):
            try:
                (k, v), = node_dict.items()
                if isinstance(k, str) and isinstance(v, list):
                    self.dict = node_dict
                else:
                    raise TypeError()
            except ValueError:
                self.dict = node_dict
        else:
            raise TypeError()

    def __str__(self):
        """
        This function returns a string representation for the node.
        node:[vertex, vertex]
        """
        return "%s" % (self.dict)


class Graph:
    """A class of graph.

    Argument:
      node_list: A list of valid nodes.
                 If no list is given, the graph is instantiated empty.

    Attributes:
        graph: A dictionary with a name of the node as a key, and a list
               of nodes which are connected to the key node as the value.
        graph_v: A dictionary with a name of the node as a key
                 and a list of nodes which connect the key node as the value.
    """
    def __init__(self, node_list=None):
        self.graph = {}
        self.graph_v = {}

        if node_list:
            for node in node_list:
                if isinstance(node, Node):
                    self.add(node)
                else:
                    raise TypeError()

    def add(self, node):
        """
        This function adds the node to the graph
        """
        (k, v), = node.dict.items()
        self.graph[k] = v
        for value in v:
            try:
                self.graph_v[value].append(k)
            except KeyError:
                self.graph_v[value] = [k]

    def delete(self, node):
        """
        This function deletes given node from the graph
        """
        (k, v), = node.dict.items()
        del self.graph[k]

    def find_path_dfs(self, start_node, end_node, path=[]):
        """
        This function returns one path between the start node and the end node.
        Search is performed Depth-First.
        """
        path = path + [start_node]
        if start_node == end_node:
            return path
        try:
            self.graph[start_node]
        except KeyError:
            return None
        for node in self.graph[start_node]:
            if node not in path:
                newpath = self.find_path_dfs(node, end_node, path)
                if newpath:
                    return newpath
        return None

    def find_all_paths(self, start_node, end_node, path=[]):
        """
        This function returns a list with all paths between the start node
        and the end node. The list is empty if no path is found.
        """
        path = path + [start_node]
        if start_node == end_node:
            return [path]
        try:
            self.graph[start_node]
        except KeyError:
            return []
        paths = []
        for node in self.graph[start_node]:
            if node not in path:
                newpaths = self.find_all_paths(node, end_node, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_shortest_path(self, start_node, end_node, path=[]):
        """
        This function returns the shortest path between the start node
        and the end node, or None if no path was found.
        """
        path = path + [start_node]
        if start_node == end_node:
            return path
        try:
            self.graph[start_node]
        except KeyError:
            return None
        shortest = None
        for node in self.graph[start_node]:
            if node not in path:
                newpath = self.find_shortest_path(node, end_node, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def has_route(self, start_node, end_node):
        """
        This function returns True if there is at least one path
        between the start node and the end node, otherwise returns False.
        """
        if self.find_path_dfs(start_node, end_node):
            return True
        else:
            return False

    def print_path(self, path):
        """
        Given the path 'A' to 'B' to 'C', print the path in following format:
        'A'->'B'->'C'
        The node names come in order.
        """
        if path:
            return "->".join("'{0}'".format(p) for p in path)
        else:
            return None

    def __str__(self):
        """
        This function returns a list representation with each node
        >>>[{'A':['B','C']},{'D':['B','C']},{'B':['C','E']}]
        """
        return str([{k: v} for (k, v) in self.graph.items()])
