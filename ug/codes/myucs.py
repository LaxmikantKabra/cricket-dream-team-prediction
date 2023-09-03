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


class Node:
    def __init__(self, state, parent, gn):
        self.state = state
        self.parent = parent
        self.gn = gn
        self.fn = self.gn
        # print(self.state, "  ",self.fn)

    def __str__(self) -> str:
        return (self.state + ' ' + self.parent.state + ' ' + str(self.gn) +
                ' ' + str(self.hn) + ' ' + str(self.fn))


def myUcs(problem, start, goal):
    pQueue = []
    root = Node(start, None, 0)
    pQueue.append(root)

    while (len(pQueue) > 0):
        node = pQueue.pop(0)
        if node.state == goal:
            cost = 0
            path = [node.state]

            while (node.parent != None):
                cost = cost + problem[node.state][node.parent.state]
                node = node.parent
                path.append(node.state)

            path.reverse()
            print('Path from start to goal is:', *path, sep=' -> ')
            print("Path cost = ", cost)
            return

        neighbours = problem[node.state]
        for neighbour in neighbours:
            newNode = Node(neighbour, node,
                           node.gn + problem[node.state][neighbour])
            pQueue.append(newNode)

        pQueue.sort(key=lambda x: x.fn)
        # print(pQueue)

    print("No path found between ", start, " and ", goal)
    return False


def main():
    print("\n\t\tHello Laxmikant\nUniform Cost Graph Search version Algorithm\n")
    start = str(input("enter start node:\t"))
    goal = str(input("enter goal node:\t"))
    problem = romania_map
    myUcs(problem, start, goal)


if __name__ == "__main__":
    main()
