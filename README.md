# Nanotopology
Novel way for finding isomorphism using nanotopology in efficient manner with retrieval of all possible isomorphic structure.

## nano_topology.py file is used to find nanosets

### Input data
1.List of all vertices of graph.

2.Dictionary that contains vertices of graph as key and adjacent vertices as value.

### Function explanation
1. Parameters of function **vh** is the list of all vertices of graph(s).
2. Parameters of function **lower_approximation** and **upper_approximation** are dictionary and the value returned by 
   function vh.   
3. Parameters of function **boundary_region** are the values returned from lower-approximation and upper_approximation.   
4. **nanoset** is obtained by passing the values returned from lower_approximation, upper_approximation and boundary_region.

## graph_equivalence.py file is used to check whether two graphs are isomorphic or not.
Dictionary that contains nodes(key) and adjacent nodes(values) of each graphs are directly passed to the equality function. 

Final result will be isomorphic vertices of second graph to the first graph if two graphs are similar else false statement(graphs are not similar) will be returned.

# Example
## Input
d1 = { 1: [1,2,4,6], 2: [1,2,3], 3: [2,3,4], 4:[1,2,4,6], 5:[4,5,6], 6:[1,5,6] } 

d2 = { a: [a,b,c,f], b: [b,e,d,a], c:[a,d,c], d:[b,c,d], e:[b,f,e], f:[e,f,a] }

## Output
two graphs are similar

matching nodes

[['a', 'c', 'd', 'b', 'e', 'f'], ['a', 'd', 'c', 'b', 'f', 'e'], ['a', 'e', 'f', 'b', 'c', 'd'], ['a', 'f', 'e', 'b', 'd', 'c'], ['b', 'c', 'd', 'a', 'e', 'f'], ['b', 'd', 'c', 'a', 'f', 'e'], ['b', 'e', 'f', 'a', 'c', 'd'], ['b', 'f', 'e', 'a', 'd', 'c']] 


# Dependencies

1.Python

2.Library - **itertools** ,it can be installed using pip.
