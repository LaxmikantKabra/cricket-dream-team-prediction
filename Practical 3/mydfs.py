romania_map = (dict(Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
                    Bucharest=dict(
                        Fagaras=211,
                        Giurgiu=90,
                        Pitesti=101,
                        Urziceni=85,
                    ),
                    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
                    Drobeta=dict(Craiova=120, Mehadia=75),
                    Eforie=dict(Hirsova=86),
                    Fagaras=dict(Bucharest=211, Sibiu=99),
                    Giurgiu=dict(Bucharest=90),
                    Hirsova=dict(Eforie=86, Urziceni=98),
                    Iasi=dict(Neamt=87, Vaslui=92),
                    Lugoj=dict(Mehadia=70, Timisoara=111),
                    Mehadia=dict(Drobeta=75, Lugoj=70),
                    Neamt=dict(Iasi=87),
                    Oradea=dict(Sibiu=151, Zerind=71),
                    Pitesti=dict(Bucharest=101, Craiova=138, Rimnicu=97),
                    Rimnicu=dict(Sibiu=80, Craiova=146, Pitesti=97),
                    Sibiu=dict(Arad=140, Fagaras=99, Oradea=151, Rimnicu=80),
                    Timisoara=dict(Arad=118, Lugoj=111),
                    Urziceni=dict(Bucharest=85, Hirsova=98, Vaslui=142),
                    Vaslui=dict(Iasi=92, Urziceni=142),
                    Zerind=dict(Arad=75, Oradea=71)))

frontier = list()
explored = list()
result = ['Not Reachable', list[:], 0]
cost = 0

def dfs_graph_search(problem, start, goal, path):
    frontier.append(start)

    while frontier:
        print(frontier)
        node = frontier.pop(0)
        explored.append(node)
        if node == goal:
            print(goal,'Goal found')
            result[0] = 'Reachable'
            return result
        for child in problem[node]:
            if child not in explored:
                temp = dfs_graph_search(problem, child, goal, path)
                if temp[0] == 'Reachable':
                    tempcost2 = problem[start][child]
                    result[2] = result[2] + tempcost2
                    # print(result)
                    path.insert(0, start)
                    break

    
    result[1] = path
    return result


def main():
    print("\n\t\t\tHello Laxmikant\nDFS Graph Search Algorithm")
    start = str(input("enter start node: "))
    goal = str(input("enter goal node: "))
    problem = romania_map
    path = []
    result = dfs_graph_search(problem, start, goal, path)
    print(result[0])
    if start == goal:
        print("Start and Goal are same, cost = 0")
        return
    if result[0] == 'Reachable':
        (result[1]).append(goal)
        print("Path from " + start + " to " + goal + " is ", *result[1], sep = ' -> ')
        print("Cost is: ", result[2])


if __name__ == "__main__":
    main()
