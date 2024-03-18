
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def adjacency_list(self):
        # converts vertices and edges of graph to an adjacency list
        adj_list = []
        # init adjacency list to store data
        for i in range(len(self.vertices)):
            # create linked list
            temp_list = LinkedList()

            # create node for first value of linked list
            temp_list.head = Node(list(self.vertices)[i])

            # re-assign to another var in order to input into for loop
            input_node = temp_list.head

            # for each vertex, create a linked list by looking at edges
            for j in range(len(self.edges)):
                if list(self.vertices)[i] in list(g.edges)[j]:
                    # create node depending on what coordinate was matched
                    if list(g.edges)[j][0] == list(self.vertices)[i]:
                        temp_node = Node(list(g.edges)[j][1])
                    if list(g.edges)[j][1] == list(self.vertices)[i]:
                        temp_node = Node(list(g.edges)[j][0])

                    # set the next value to be this new node
                    input_node.next = temp_node

                    # set the next input to be the newly created node
                    input_node = temp_node

            # assign this list to the adj_list
            adj_list.append(temp_list)

        # print out the whole adjacency list once complete
        for ll in adj_list:
            # assign traversing node to var
            head = ll.head
            print(f'for {head.value}, list is {head.value}-')
            # iterate until head.next is null
            while head.next:
                print(f'{head.next.value}')
                # assign next node to new head
                head = head.next
            print('\n')



V = {0,1,2,3}
E = {(0,1), (0,2), (0,3), (1,2)}

g = Graph(V, E)

g.adjacency_list()