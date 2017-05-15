def mat1(filename):
	f = open(filename, 'r')
	mat = []
	for line in f:
		mat.append(line.strip().split())
	for i in range(len(mat)):
		for j in range(len(mat[i])):
			mat[i][j] = int(mat[i][j])
	return mat

if __name__ == "__main__":
	filename = "matriz1.txt"
	mat = mat1(filename)
	print mat[0]
