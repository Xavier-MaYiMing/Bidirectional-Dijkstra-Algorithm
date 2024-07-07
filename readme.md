### The Bi-Directional Dijkstra Algorithm for the Shortest Path Problem

##### Reference: [Efficient point-to-point shortest path algorithms](https://www.cs.princeton.edu/courses/archive/spr06/cos423/Handouts/EPP%20shortest%20path%20algorithms.pdf)

The bi-directional Dijkstra algorithm is much more efficient that the origin Dijkstra algorithm.

| Variables            | Meaning                                                      |
| -------------------- | ------------------------------------------------------------ |
| graph                | The original graph                                           |
| reversed_graph       | The reversed graph                                           |
| source               | The source node                                              |
| target               | The target node                                              |
| dist_f, dist_b       | The distance label in the forward and backward search        |
| path_f, path_b       | The path label in the forward and backward search            |
| queue_f, queue_b     | The heap in the forward and backward search                  |
| visited_f, visited_b | The list of scanned nodes in the forward and backward search |
| mu                   | The length of the best path                                  |

### Bi-directional Dijkstra algorithm's pseudocode

> Maintain a forward distance label $d_f(v)$ and a backward distance label $d_b(v)$ for each vertex. Maintain the length of the best path $\mu$ and set $\mu = \infty$.
>
> > Initially, $d_f(s) = 0$ and $d_f(v) = \infty$ for all other vertices. Similarly, $d_b(t) = 0$ and $d_b(v) = \infty$​ for all other vertices.
> >
> > In each iteration contains forward and backward search:
> >
> > > Pick an unscanned vertex $v$ with the smallest $d_f(\cdot)$ and perform the forward search.
> > >
> > > > For each edge $(v, w)$ on the original graph, check if $d_f(w) > d_f(v) + l(v, w)$.
> > > >
> > > > If it is, set $d_f(w) \leftarrow d_f(v) + l(v, w)$​.
> > > >
> > > > If $w$ has been scanned in the backward search and $d_f(v) + l(v, w) + d_b(w) < \mu$, set $\mu \leftarrow d_f(v) + l(v, w) + d_b(w)$​.
> > >
> > > Pick an unscanned vertex $v$ with the smallest $d_b(\cdot)$ and perform the backward search.
> > >
> > > > For each edge $(v, w)$ on the reversed graph, check if $d_b(w) > d_b(v) + l(w, v)$.
> > > >
> > > > If it is, set $d_b(w) \leftarrow d_b(v) + l(w, v)$.
> > > >
> > > > If $w$ has been scanned in the forward search and $d_b(v) + l(w, v) + d_b(w) < \mu$, set $\mu \leftarrow d_b(v) + l(w, v) + d_b(w)$.
> > >
> > > Termination condition: Let $top_f$ and $top_b$ be the top heap values of forward and backward heaps, if $top_f + top_b \leq \mu$​, the algorithm terminates.





#### Example

```python
if __name__ == '__main__':
    test_graph = {
        0: {1: 62, 2: 44, 3: 67},
        1: {0: 62, 2: 32, 4: 52},
        2: {0: 44, 1: 33, 3: 32, 4: 52},
        3: {0: 67, 2: 32, 4: 54},
        4: {1: 52, 2: 52, 3: 54}
    }
    s = 0
    d = 4
    print(main(test_graph, s, d))
```

#### Output

```python
{'length': 96, 'path': [0, 2, 4]}
```

