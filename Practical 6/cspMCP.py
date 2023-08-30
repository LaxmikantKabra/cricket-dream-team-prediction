def check_valid(graph):
    for node, nexts in graph.items():
        assert (nexts)  # no isolated node
        assert (node not in nexts)  # # no node linked to itself
        for next in nexts:
            assert (next in graph and node in graph[next]
                    )  # A linked to B implies B linked to A


class MapColor:
    def __init__(self, graph, colors):
        self.graph = graph
        check_valid(graph)
        nodes = list(self.graph.keys())
        self.node_colors = {node: None for node in nodes}
        self.domains = {node: set(colors) for node in nodes}

    def solve(self):
        uncolored_nodes = [
            n for n, c in self.node_colors.items() if c is None
        ]
        if not uncolored_nodes:
            print(self.node_colors)
            return True

        node = uncolored_nodes[0]
        print('domain for ' + node + ': ' + str(self.domains[node]))
        for color in self.domains[node].copy():
            if all(color != self.node_colors[n] for n in self.graph[node]):
                self.set_color(node, color)
                self.remove_from_domains(node, color)

                if self.solve():
                    return True

                self.set_color(node, None)
                self.add_to_domains(node, color)

        return False

    def set_color(self, key, color):
        self.node_colors[key] = color

    def remove_from_domains(self, key, color):
        for node in self.graph[key]:
            if color in self.domains[node]:
                self.domains[node].remove(color)

    def add_to_domains(self, key, color):
        for node in self.graph[key]:
            self.domains[node].add(color)


WA = 'western australia'
NT = 'northwest territories'
SA = 'southern australia'
Q = 'queensland'
NSW = 'new south wales'
V = 'victoria'
T = 'tasmania'

colors = {'red', 'green', 'blue'}

australia = {
    T: {V},
    WA: {NT, SA},
    NT: {WA, Q, SA},
    SA: {WA, NT, Q, NSW, V},
    Q: {NT, SA, NSW},
    NSW: {Q, SA, V},
    V: {SA, NSW, T}
}

problem = MapColor(australia, colors)

problem.solve()
