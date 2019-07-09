import networkx as nx

def pagerank(G, alpha=0.85, personalization=None,
             max_i=100, nstart=None, weight='weight',
             dangling=None):

    #nothing in our graph
    if len(G) == 0:
        return {}
    #turns graph directed
    if not G.is_directed():
        D = G.to_directed()
    else:
        D = G

    # Create a copy of our matrix satisfying our properties (positivity, single eigenvalue)
    W = nx.stochastic_graph(D, weight=weight)
    N = W.number_of_nodes()

        #x is our starting trial eigenvector
        x = dict.fromkeys(W, 1.0 / N)

        p = dict.fromkeys(W, 1.0 / N)

    if dangling is None:

        # Use p if dangling vector not specified
        dangling_weights = p
    else:
        missing = set(G) - set(dangling)
        if missing:
            raise NetworkXError('Dangling node dictionary '
                                'must have a value for every node. '
                                'Missing nodes %s' % missing)
        s = float(sum(dangling.values()))
        dangling_weights = dict((k, v/s) for k, v in dangling.items())
    dangling_nodes = [n for n in W if W.out_degree(n, weight=weight) == 0.0]

    # power iteration: make up to max_i iterations
    for _ in range(max_iter):
        xlast = x
        x = dict.fromkeys(xlast.keys(), 0)
        danglesum = alpha * sum(xlast[n] for n in dangling_nodes)
        for n in x:

            # this matrix multiply is different because we're
            # left-multiplying x^T=xlast^T*W
            for nbr in W[n]:
                x[nbr] += alpha * xlast[n] * W[n][nbr][weight]
            x[n] += danglesum * dangling_weights[n] + (1.0 - alpha) * p[n]

        # check convergence, and if normalized
        err = sum([abs(x[n] - xlast[n]) for n in x])
        if err < N*tol:
            return x
    raise NetworkXError('pagerank: power iteration failed to converge '
                        'in %d iterations.' % max_iter)
