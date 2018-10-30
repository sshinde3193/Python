from collections import deque

def read_words(word_file):
    '''
    This function reads the words which are the vertices and stores the hashed word combinations of each word into the dictionary as keys
    :param word_file: 
    :precondition: The file containing the words must exist
    :postcondition: A dictionary is created with all the hashed words and their buckets
    :return: The graph of the hashed words with buckets
    :complexity: Best Case = Worst Case = O(n^2), where n is the total number of words
    '''

    file = open(word_file, 'r')
    bucket_graph = dict()
    for word in file:
        for i in range(len(word)-1):
            word = word.strip('\n')
            new_word = (word[:i] + '#' + word[i+1:]).strip('\n')
            if new_word in bucket_graph:
                bucket_graph[new_word].append(word)
            else:
                bucket_graph[new_word] = [word]
    return bucket_graph

def construct_adj_list(bucket_graph):
    '''
    This function creates the graph for the words with its adjacency lists
    :param bucket_graph: 
    :precondition: The graph of the bucket hashed values must have already been created
    :postcondition: The word_graph is created with the words as keys and their respective word edges in an adjacency list
    :return: The word graph is returned
    :complexity: Best Case = Worst Case = O(n^2), where n is the length of the graph
    '''

    word_graph = dict()
    for word in bucket_graph:
        list = bucket_graph[word]
        for vertex in range(len(list)):
            if list[vertex] not in word_graph:
                word_graph[list[vertex]] = []
            for v in range(len(list)):
                if list[vertex] != list[v]:
                    word_graph[list[vertex]].append(list[v])
    return word_graph

def bfs_component(word_graph):
    '''
    This function finds the required components of the words
    :param word_graph: 
    :precondition: The word_graph must have already been created
    :postcondition: The components are created
    :return: The respective component is returned
    :complexity: Best Case = Worst Case = O(n^2), where n is the length of word graph
    '''

    visited_vertices = dict()
    component = dict()
    start_vertex, neighbours = word_graph.popitem()
    queue = deque([start_vertex])
    word_graph[start_vertex] = neighbours
    while len(queue) != 0:                                  # while queue is not empty or end marker has not reached
        front_vertex = queue.popleft()
        if front_vertex not in word_graph:
            continue
        visited_vertices[front_vertex] = True
        component[front_vertex] = word_graph[front_vertex]
        for vertex in word_graph[front_vertex]:                           #front_vertex's adjacency list
            if not visited_vertices.get(vertex, False):
                queue.append(vertex)
                component[vertex] = neighbours
        word_graph.pop(front_vertex)
    return component

def components(word_graph):
    '''
    This function appends the components and their respective keys into a list
    :param word_graph: 
    :precondition: The bfs for each component must have already been constructed
    :postcondition: The component and keys lists are created
    :return: component and key list
    :complexity: Best Case = Worst Case = O(n^2), where n is the length of the word graph
    '''

    comps = []
    keys = []
    while len(word_graph) != 0:
        comps.append(bfs_component(word_graph))
        for key in comps:
            keys.append(key)
    return comps, keys

def bfs_diameter(component_list, keys):
    '''
    This function finds the diameter of the required components of the words
    :param word_graph: 
    :precondition: The components must have already been created
    :postcondition: The diameter for each of the components is found
    :return: The respective diameter for the respective component is returned
    :complexity: Best Case = Worst Case = O(n^2), where n is the length of word graph
    '''

    visited_vertices = dict()
    distance = dict()
    start_vertex = 0
    queue = deque([keys[start_vertex]])
    distance[start_vertex] = 0
    while len(queue) != 0:
        front_vertex = queue.popleft()
        if front_vertex not in word_graph:
            continue
        visited_vertices[front_vertex] = True
        visited_vertices[front_vertex] = component_list[front_vertex]
        for vertex in component_list[front_vertex]:
            if not visited_vertices.get(vertex, False) and not distance.get(vertex, False):
                queue.append(vertex)
                distance[vertex] = distance[front_vertex] + 1
    return distance

if __name__ == '__main__':
    word_file = input('Enter a filename: ')
    bucket_graph = read_words(word_file)
    word_graph = construct_adj_list(bucket_graph)
    component_list, keys = components(word_graph)
