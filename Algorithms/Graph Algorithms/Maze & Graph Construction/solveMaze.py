from collections import deque

def maze_to_maze_graph(m_file):
    '''
    This function constructs the maze_graph online by reading one row of the maze at a time and keeping only the previous row in memory 
    :param: Any supplied text file containing a maze
    :precondition: The text file must contain a maze
    :postcondition: A maze_graph is constructed which stores a marker, column and adjacency list for each vertex v
    :return: The whole maze_graph, the entry & exit point of the maze_graph, the length of the row, and the starting and ending vertices of each row 
    :complexity: Best Case = Worst Case = O(n^2), where n is the length of the row
    '''

    maze_file = open(m_file, 'r')
    row_c = 0
    vertex_c = 0
    start_vertex = None
    end_vertex = None
    maze_graph = []
    previous_row = []
    row_markers = []
    for row in maze_file:
        current_row = [None] * (len(row)-1)
        for col in range(len(row)):
            if col == 0:
                row_markers.append(vertex_c)
            elif col == len(row) - 1:
                row_markers.append(vertex_c - 1)
            if row[col] in '.SF':
                maze_graph.append([False, col, []])
                current_row[col] = vertex_c
                if row[col] == 'F':
                    end_vertex = vertex_c
                elif row[col] == 'S':
                    start_vertex = vertex_c
                if row[col-1] in '.SF':                  # checks for west vertex
                    maze_graph[vertex_c][2].append(vertex_c-1)
                    maze_graph[vertex_c-1][2].append(vertex_c)
                    vertex_c += 1
                else:
                    vertex_c += 1
                if row_c > 0 and previous_row[col] is not None:       # checks for north vertex
                    maze_graph[vertex_c-1][2].append(previous_row[col])
                    maze_graph[previous_row[col]][2].append(vertex_c-1)
        previous_row = current_row
        row_c += 1
    row_len = len(row) - 1
    return maze_graph, start_vertex, end_vertex, row_markers, row_len

def shortest_path_bfs(maze_graph, start_vertex):
    '''
    This function finds the shortest path from the starting vertex to every other reachable vertex in the maze_graph
    :param: maze_graph and the starting vertex
    :precondition: The maze_graph must already have been constructed
    :postcondition: The shortest paths are found from the start to every other vertex by traversing through the whole maze_graph and going through each vertex
    :return: The vertex list of predecessors
    :complexity: Best Case = Worst Case = O(n*m), where n is the length of the maze and m is the length of the adjacency list
    '''

    visited_vertices = [False] * len(maze_graph)
    predecessors = [None] * len(maze_graph)
    inqueue = [False] * len(maze_graph)
    queue = deque([start_vertex])
    visited_vertices[start_vertex] = True
    while len(queue) != 0:                                  # while queue is not empty or end marker has not reached
        front_vertex = queue.popleft()
        visited_vertices[front_vertex] = True
        inqueue[front_vertex] = False
        for vertex in maze_graph[front_vertex][2]:               #front_vertex's adjacencylist
            if visited_vertices[vertex] is False and inqueue[vertex] is False:
                predecessors[vertex] = front_vertex
                queue.append(vertex)
                inqueue[vertex] = True
    return predecessors

def mark_maze_graph_path(maze_graph, end_vertex, predecessors):
    '''
    This function marks the vertices on the maze_graph which are on the shortest path between the exit and entry point
    :param: maze_graph, exit vertex and predecessors vertex list
    :precondition: The predecessor list must have already been constructed
    :postcondition: The vertices which are on the shortest path are marked
    :return: An updated maze_graph is returned with the updated mark boolean values for the vertices on the shortest path
    :complexity: Best Case = Worst Case = O(n), where n is the length of the predecessors list
    '''

    maze_graph[end_vertex][0] = True
    while predecessors[end_vertex] is not None:
        maze_graph[predecessors[end_vertex]][0] = True
        end_vertex = predecessors[end_vertex]
    return maze_graph

def write_file(marked_maze_graph, row_markers, row_len):
    '''
    This function writes the maze back to the file containing the shortest path solution denoted by the path of 'o's
    :param: marked maze_graph with the shortest path, row_markers containing start and end vertex of each row, and width of the row
    :precondition: The maze_graph and row markers list must have already been constructed
    :postcondition: The maze with the shortest path is written to the output file
    :return: None
    :complexity: Best Case = Worst Case = O(n^2), where n is the number of rows
    '''

    file = open('solution.txt', 'w')
    for j in range(0, len(row_markers), 2):
        row = ['#'] * row_len
        for i in range(row_markers[j], row_markers[j+1]+1):
            if marked_maze_graph[i][0] is False:
                row[maze_graph[i][1]] = '.'
            else:
                row[maze_graph[i][1]] = 'o'
        for k in range(len(row)):
            file.write(row[k])
        file.write('\n')

if __name__ == '__main__':
    m_file = input('Enter the filename: ')
    maze_graph, start_vertex, end_vertex, row_markers, row_len = maze_to_maze_graph(m_file)
    predecessors = shortest_path_bfs(maze_graph, start_vertex)
    marked_maze_graph = mark_maze_graph_path(maze_graph, end_vertex, predecessors)
    write_file(maze_graph, row_markers, row_len)
