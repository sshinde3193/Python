def initialise_d_graph(m, n):
    '''
    This function initialises an empty d graph
    :param m: m is the first letters in the alphabet
    :param n: size of the string
    :precondition: None
    :postcondition: D-graph is initalised
    :return: initalised d graph with empty adj lists
    :complexity: Best Case = Worst Case = O(m**n), exponential time complexity
    '''

    d_graph = []
    for i in range(m ** n):
        d_graph.append([])
    return d_graph

def create_d_graph(m, initial_d_graph):
    '''
    This function creates the d-graph in base-m
    :param m: m is the first letters in the alphabet
    :param initial_d_graph: takes the initalises dgraph
    :precondition: the d graph must be initalised
    :postcondition: the filled out d-graph is constructed
    :return: the d-graph is returned
    :complexity: Best Case = Worst Case = O(n^2), where n is the length of the d graph
    '''

    for i in range(len(initial_d_graph)):
        vertex = (i % (m ** (n - 1)))
        connections = vertex * m
        for j in range(m):
            initial_d_graph[i].append(connections + j)
    return initial_d_graph

def find_path_dfs(d_graph, source_vertex):
    '''
    This function does depth first search recursively to find the path
    :param d_graph: d-graph with adj lists
    :param source_vertex: starting vertex
    :precondition: the d-graph must already have been constructed
    :postcondition: the path_list is found
    :return: path list is returned
    :complexity: Best Case = Worst Case = O(E), where e is the number of edges
    '''

    path_list = []
    current = d_graph[source_vertex].pop()
    while source_vertex != current:
        path_list.append(current)
        current = d_graph[current].pop()
    path_list.append(source_vertex)
    return path_list

def convert_to_character(paths, m):
    '''
    This function converts the path to the characters and writes to the output file
    :param paths: path to write to file
    :param m: m is the first letters in the alphabet
    :precondition: the paths must be calculated
    :postcondition: the output is written to the file
    :return: None
    '''

    file = open('outputTask1.txt', 'w')
    for i in range(len(paths)):
        char = paths[i] % m
        write_char = chr(97 + char)
        file.write(write_char)

if __name__ == '__main__':
    m = int(input('Enter the number of letters m: '))
    n = int(input('Enter the size of the string n: '))
    if 2 <= m <= 5 and 2 <= n <= 3:
        initial_d_graph = initialise_d_graph(m, n)
        d_graph = create_d_graph(m, initial_d_graph)
        paths = find_path_dfs(d_graph, 0)
        i = 0
        while i < len(paths):
            if d_graph[paths[i]] != []:
                new_path = find_path_dfs(d_graph, paths[i])
                paths = paths[:i+1] + new_path + paths[i+1:]
            else:
                i += 1
        convert_to_character(paths, m)
    else:
        raise ValueError
