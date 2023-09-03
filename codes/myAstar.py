import math

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

romania_map_locations = dict(Arad=(91, 492),
                             Bucharest=(400, 327),
                             Craiova=(253, 288),
                             Drobeta=(165, 299),
                             Eforie=(562, 293),
                             Fagaras=(305, 449),
                             Giurgiu=(375, 270),
                             Hirsova=(534, 350),
                             Iasi=(473, 506),
                             Lugoj=(165, 379),
                             Mehadia=(168, 339),
                             Neamt=(406, 537),
                             Oradea=(131, 571),
                             Pitesti=(320, 368),
                             Rimnicu=(233, 410),
                             Sibiu=(207, 457),
                             Timisoara=(94, 410),
                             Urziceni=(456, 350),
                             Vaslui=(509, 444),
                             Zerind=(108, 531))


class Node:
    def __init__(self, state, parent, gn, hn):
        self.state = state
        self.parent = parent
        self.gn = gn
        self.hn = hn
        self.fn = gn + hn
        # print(self.fn)

    def __str__(self) -> str:
        return (self.state + ' ' + self.parent.state + ' ' + str(self.gn) +
                ' ' + str(self.hn) + ' ' + str(self.fn))


def myAstar(problem, start, goal):
    pQueue = []
    root = Node(start, None, 0, 0)
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
            x2 = (romania_map_locations[goal][0] -
                  romania_map_locations[neighbour][0])**2
            y2 = (romania_map_locations[goal][1] -
                  romania_map_locations[neighbour][1])**2
            hn = int(math.sqrt(x2 + y2))
            '''formula that will calculate straight line distance and put it in hn'''
            newNode = Node(neighbour, node,
                           node.gn + problem[node.state][neighbour], hn)
            pQueue.append(newNode)

        pQueue.sort(key=lambda x: x.fn)

    print("No path found between ", start, " and ", goal)
    return False


def main():
    print("\n\t\tHello Laxmikant\n\tA* Graph Search Algorithm\n")
    start = str(input("enter start node:  "))
    goal = str(input("enter goal node:  "))
    problem = romania_map
    myAstar(problem, start, goal)


if __name__ == "__main__":
    main()
