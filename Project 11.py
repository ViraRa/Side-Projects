from collections import deque 
class Graphs:

    def __init__(self, node_list, is_directed=False):
        self.nodes = node_list
        self.adj_list = {}
        self.check = is_directed

        for node in node_list:
            self.adj_list[node] = []

    def __str__(self): # to prints the adj_list in a more readable format 
        for key, value in self.adj_list.items():
            print(str(key) + "->" + str(value))

    def add_edge(self, u, v):
        if self.check == False: # undirected
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        else: # diagraph
            self.adj_list[u].append(v)

    def in_degree(self, node): # finds how many adj_nodes are pointing to the specified node
        count = 0
        if self.check == False: 
            return len(self.adj_list[node])
        else:
            for value in self.adj_list.values():
                if(node in value):
                    count +=1
            return count
    
    def out_degree(self, node): # finds how many adj_nodes are pointing away from the specified node
        return len(self.adj_list[node])

    def BFS(self):

        # no need to check if there are adjacent nodes in adj_list since constructor require a 
        # node_list. Nodes that are not connected still make up a graph

        Queue = deque([])
        Queue.append(self.nodes[0])

        visited = [False] * len(self.nodes) # setting the boolean array to all False
        visited[0] = True # appended to Queue so mark this as True

        BFS_list = []

        while Queue: 
            adj_node = Queue.popleft() # remove from Queue on the left side
            BFS_list.append(adj_node) # contains the BFS sequence

            # for loop to look into the dictionary using the adj_node as key
            # If not visited then append to Queue otherwise don't
            for node in self.adj_list[adj_node]:
                if visited[self.nodes.index(node)] == False:
                    Queue.append(node)
                    visited[self.nodes.index(node)] =  True         
        
        return BFS_list

    def DFS(self):
    
        # no need to check if there are adjacent nodes in adj_list since constructor require a 
        # node_list. Nodes that are not connected still make up a graph
        
        visited = [False] * len(self.nodes)
        DFS_list = []

        return self.DFS_helper(visited, DFS_list, self.nodes[0])

    def DFS_helper(self, visted_arr, DFS_list, curr_node):

        visted_arr[self.nodes.index(curr_node)] = True
        DFS_list.append(curr_node)

        # very similar to BFS code but recursive
        for node in self.adj_list[curr_node]:
            if visted_arr[self.nodes.index(node)] == False:
                # if not visted then vist it using recursive calls
                self.DFS_helper(visted_arr, DFS_list, node)

        return DFS_list
        
 ######################################################### Unit test ###############################################################
 
import unittest
from Graph import Graphs

class Test_Graph(unittest.TestCase):

    # Testing Graph.py

    @classmethod
    def setUpClass(cls):
        
        node = ["A", "B", "C", "D", "C", "E", "F"]
        cls.graph = Graphs(node) # undirected
        cls.graph1 = Graphs(node, True) # directed (diagraph)

        edge_list = [ ("A", "B"), ("A", "D"), ("B", "C"),("D", "C"),("D", "E"), ("C", "F"), ("E", "F")]

        for u, v in edge_list:
            cls.graph.add_edge(u, v)
            cls.graph1.add_edge(u, v)

    def test_add_edge(self):
        
        # Testing undirected graph
        self.assertEqual(self.graph.adj_list["A"], ["B", "D"])
        self.assertEqual(self.graph.adj_list["D"], ["A", "C", "E"])

        # Testing directed graph
        self.assertEqual(self.graph1.adj_list["B"], ["C"])
        self.assertEqual(self.graph1.adj_list["D"], ["C", "E"])
        self.assertEqual(self.graph1.adj_list["A"], ["B", "D"])

    def test_in_degree(self):
        
        # Testing undirected graph
        self.assertEqual(self.graph.in_degree("C"), 3)
        self.assertEqual(self.graph.in_degree("A"), 2)
        self.assertEqual(self.graph.in_degree("F"), 2)
        
        # Testing directed graph
        self.assertEqual(self.graph1.in_degree("C"), 2)
        self.assertEqual(self.graph1.in_degree("A"), 0)
        self.assertEqual(self.graph1.in_degree("F"), 2)


    def test_out_degree(self):
        
        #Testing undirected graph
        self.assertEqual(self.graph.out_degree("C"), 3)
        self.assertEqual(self.graph.out_degree("A"), 2)
        self.assertEqual(self.graph.out_degree("F"), 2)

        #Testing directed graph
        self.assertEqual(self.graph1.out_degree("D"), 2)
        self.assertEqual(self.graph1.out_degree("E"), 1)
        self.assertEqual(self.graph1.out_degree("B"), 1)

    def test_BFS(self):
        #Testing undirected graph since the result is the same as directed graph
        self.assertEqual(self.graph.BFS(), ["A", "B", "D", "C", "E", "F"])

    def test_DFS(self):
        #Testing undirected graph
        self.assertEqual(self.graph.DFS(), ["A", "B", "C", "D", "E", "F"])

        #Testing directed graph
        self.assertEqual(self.graph1.DFS(), ["A", "B", "C", "F", "D", "E"])

      
if __name__ == "__main__":
    unittest.main()
