import numpy as np
import cvxpy as cp 
import random
import numpy.linalg as npl
import sys

SCALE = 2

def main():

	fp  = open('input.txt', 'r')

	no_partitions = int(fp.readline())

	Q = np.zeros((no_partitions, no_partitions), dtype=int)
	for i in range(no_partitions):
		Q[i] = np.array(list(map(int, fp.readline().split())))

	Z = np.zeros((no_partitions, no_partitions), dtype=int)
	for i in range(no_partitions):
		Z[i] = np.array(list(map(int, fp.readline().split())))

	fp.close()

	no_pair = no_partitions*(no_partitions-1)

	A = np.zeros((no_pair, no_partitions), dtype=int)
	N_L = np.zeros((no_partitions,1))

	x = 0
	for i in range(no_partitions):
		for j in range(no_partitions):
			if i!=j:
				A[x][i] = Q[i][j]
				A[x][j] = -Z[j][i]
				x+=1

	for i in range(0,no_partitions):
		mx = Q[i][i]+1
		for j in range(no_partitions):
				mx = max(mx,Q[j][i])
				mx = max(mx, Z[i][j])
		N_L[i] = mx

	is_fesiable = True
	if(npl.matrix_rank(A)==no_partitions):
		is_fesiable = False

	for i in range(no_partitions):
		if Q[i][i] != Z[i][i]:
			is_fesiable = False

	if not is_fesiable:
		sys.exit(1)

	N = cp.Variable((no_partitions,1), integer=True)
	C = np.random.randint(2,size=(1,no_partitions))

	obj = cp.Minimize(C@N)
	cons = [A@N==0,
			N>=N_L]

	prob = cp.Problem(obj, cons)
	prob.solve()

	N_ans = np.array(np.round_(N.value), dtype=int).T
        
	gcd = np.gcd.reduce(N_ans)

	N_ans = np.true_divide(N_ans, gcd)
	scale = np.ceil(np.amax(np.divide(N_L.T[0], N_ans)))

	N_ans = N_ans*scale*SCALE
	print(N_ans[0])
	fp  = open('temp.txt', 'a')
	fp.write('\n')
	for i in N_ans[0]:
		fp.write(str(int(i)) + " ")
	fp.close()


if __name__ == '__main__':
	main()
