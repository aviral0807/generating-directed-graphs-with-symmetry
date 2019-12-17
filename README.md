# btp

This is a project to generate directed graphs with prescribed equitable partition whose MBC coincides with its OAG.

1. Input needs to be enter into `input.txt`. First line contains one integer representing the number of partitions p, next p line represents X-matrix and next p lines represent Y-matrix representing the quotient graph for which the graph needs to be generated, next line contains one integer representing the scale s.
```
2           #p (no. of partitions)
1 3         #X-matrix
2 1
1 2         #Y-matrix
3 1
2           #s (scale)
```
2. Run command `./run.sh`
3. Check the output in `output.txt`
