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
        return [mat2,tasks_per_machine]

def mat3(matriz1,matriz2,tasks_per_machine):
		ordemlinhas = []

		#Primeira Linha

		maior = 0
		for i in xrange(1,len(tasks_per_machine)):
			if tasks_per_machine[i] > tasks_per_machine[maior]:
				maior = i
		ordemlinhas.append(maior)

		#Restante das Linhas
		while(len(ordemlinhas)<len(tasks_per_machine)):
			i = ordemlinhas[-1]
			for j in xrange(len(tasks_per_machine)):
				if j not in ordemlinhas:
					maior = j
					break
			for j in xrange(len(tasks_per_machine)):
				if j not in ordemlinhas:
					if matriz2[i][j] > matriz2[i][maior]:
						maior = j
					elif matriz2[i][j] == matriz2[i][maior]:
						if tasks_per_machine[j] > tasks_per_machine[maior]:
							maior = j
			ordemlinhas.append(maior)

		#Construcao da nova matriz com as linhas reordenadas2
		novaMat = []
		for i in ordemlinhas:
			novaMat.append(matriz1[i])

		return [novaMat,ordemlinhas]

if __name__ == "__main__":
        filename = "matriz1.txt"	
        matriz1 = mat1(filename)
        print 'Matriz A'
        for i in matriz1:
        	print i
        matriz2,tasks_per_machine = mat2(filename)
        print
        for i in xrange(len(tasks_per_machine)):
        	matriz2[i].append('|')
        	matriz2[i].append(tasks_per_machine[i])
        print "Matriz B"
        for i in matriz2:
        	print i
        print
        nova,ordemlinhas = mat3(matriz1,matriz2,tasks_per_machine)
        print ordemlinhas
        print
        print 'Matriz A com as linhas atualizadas'
        for i in nova:
        	print i
