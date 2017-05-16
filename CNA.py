def mat1(filename):
        f = open(filename, 'r')
        mat = []
        for line in f:
                mat.append(line.strip().split())
        for i in range(len(mat)):
                for j in range(len(mat[i])):
                        mat[i][j] = int(mat[i][j])
        return mat

def mat2(filename):
        mat = mat1(filename)
        tasks_per_machine = [0]*len(mat)
        mat2 = []
        for _ in range(len(mat)):
                mat2.append([0]*len(mat))
        for i in range((len(mat) - 1)):
                for m in range(i + 1, len(mat)):
                        for j in range(len(mat[i])):
                                        if mat[i][j] == 1 and mat[m][j] == 1:
                                                tasks_per_machine[i] += 1
                                                tasks_per_machine[m] += 1
                                                mat2[i][m] += 1
                                                mat2[m][i] += 1
        return tasks_per_machine

if __name__ == "__main__":
        filename = "matriz1.txt"
        mat = mat2(filename)
        for line in mat:
                print line
