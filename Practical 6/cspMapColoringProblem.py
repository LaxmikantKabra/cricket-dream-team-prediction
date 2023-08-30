def check_valid(graph):
    for node, nexts in graph.items():
        assert (node not in nexts)  # # no node linked to itself
        for next in nexts:
            assert (next in graph and node in graph[next]
                    )  # A linked to B implies B linked to A


def check_solution(graph, solution):
    if solution is not None:
        for node, nexts in graph.items():
            assert (node in solution)
            color = solution[node]
            for next in nexts:
                assert (next in solution and solution[next] != color)


def find_best_candidate(graph, guesses):
    if True:  #optimised
        # Optimisations are to be put here. Ideas would be to take the node with the most
        # uncolored neighboors or the one with the smallest possible number of colors or both
        candidates_with_add_info = [
            (
                -len({
                    guesses[neigh]
                    for neigh in graph[n] if neigh in guesses
                }),  # nb_forbidden_colors
                -len({neigh
                      for neigh in graph[n] if neigh not in guesses
                      }),  # minus nb_uncolored_neighbour
                n) for n in graph if n not in guesses
        ]
        candidates_with_add_info.sort()
        candidates = [n for _, _, n in candidates_with_add_info]
    else:
        candidates = [n for n in graph if n not in guesses]
        candidates.sort()  # just to have some consistent performances
    if candidates:
        candidate = candidates[0]
        assert (candidate not in guesses)
        return candidate
    assert (set(graph.keys()) == set(guesses.keys()))
    return None


nb_calls = 0


def solve(graph, colors, guesses, depth):
    global nb_calls
    nb_calls += 1
    n = find_best_candidate(graph, guesses)
    if n is None:
        return guesses  # Solution is found
    for c in colors - {
            guesses[neigh]
            for neigh in graph[n] if neigh in guesses
    }:
        assert (n not in guesses)
        assert (all((neigh not in guesses or guesses[neigh] != c)
                    for neigh in graph[n]))
        guesses[n] = c
        indent = '  ' * depth
        print("%sTrying to give color %s to %s" % (indent, c, n))
        if solve(graph, colors, guesses, depth + 1):
            print("%sGave color %s to %s" % (indent, c, n))
            return guesses
        else:
            del guesses[n]
            print("%sCannot give color %s to %s" % (indent, c, n))
    return None


def solve_problem(graph, colors):
    check_valid(graph)
    solution = solve(graph, colors, dict(), 0)
    print(solution)
    check_solution(graph, solution)


WA = 'western australia'
NT = 'northwest territories'
SA = 'southern australia'
Q = 'queensland'
NSW = 'new south wales'
V = 'victoria'
T = 'tasmania'

australia = {
    T: {V},
    WA: {NT, SA},
    NT: {WA, Q, SA},
    SA: {WA, NT, Q, NSW, V},
    Q: {NT, SA, NSW},
    NSW: {Q, SA, V},
    V: {SA, NSW, T}
}

colors = {'red', 'green', 'blue'}

solve_problem(australia, colors)
print(nb_calls)
