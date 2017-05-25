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
                linhas = len(tasks_per_machine)
                        
                #Primeira Linha
                maior = 0
                for i in xrange(1,linhas):
                        if tasks_per_machine[i] > tasks_per_machine[maior]:
                                maior = i
                ordemlinhas.append(maior)

                #Restante das Linhas
                while(len(ordemlinhas)<linhas):

                        #Acesso a ultima linha adicionada
                        i = ordemlinhas[-1]

                        #Definindo que o maior elemento a principio sera
                        #o primeiro nao adicionado ainda
                        for j in xrange(linhas):
                                if j not in ordemlinhas:
                                        maior = j
                                        break

                        #Detecta o maior elemento da linha e em caso de empate
                        #escolhe o que tiver maior tasks_per_machine
                        for j in xrange(linhas):
                                if j not in ordemlinhas:
                                        if matriz2[i][j] > matriz2[i][maior]:
                                                maior = j
                                        elif matriz2[i][j] == matriz2[i][maior]:
                                                if tasks_per_machine[j] > tasks_per_machine[maior]:
                                                        maior = j
                        ordemlinhas.append(maior)
                        
                #Construcao da nova matriz com as linhas reordenadas
                novaMat = []
                for i in ordemlinhas:
                        novaMat.append(matriz1[i])

                return [novaMat,ordemlinhas]

def contagem(seq, coluna):
        cont = 0
        for linha in seq:
                if linha[coluna] == 1:
                        cont += 1
        return cont

def mat4(matriz3):
        mat = matriz3[:]
        ordemColunas = []
        colunas = len(mat[0])
        
        while True:

                #Se a matriz ainda esta divisivel
                if len(mat) > 1:
                        div = len(mat)/2
                        seq1 = mat[:div]
                        seq2 = mat [div:]

                        #Adiciona a coluna na nova ordem se o numero de 1s
                        #na coluna for maior em SEQ1 que em SEQ2
                        for j in xrange(colunas):
                                if j not in ordemColunas:
                                        n1 = contagem(seq1,j)
                                        n2 = contagem(seq2,j)
                                        if n1 > n2:
                                                ordemColunas.append(j)

                        #Se todas as linhas ja foram marcadas o processo para,
                        #caso contrario a nova matriz sera SEQ2
                        if len(ordemColunas) == colunas:
                                break
                        else:
                                mat = seq2
                                
                #Caso nao seja mais possivel dividir a matriz
                #adicionam-se as linhas restantes diretamente
                else:
                        for j in xrange(colunas):
                                if j not in ordemColunas:
                                        ordemColunas.append(j)
                        break

        #Construcao da nova matriz, com linhas e colunas rearranjadas
        novaMat = []
        for i in matriz3:
                linha = []
                for j in ordemColunas:
                        linha.append(i[j])
                novaMat.append(linha)

        return [novaMat,ordemColunas]
                

if __name__ == "__main__":
        filename = "matriz1.txt"
        
        matriz1 = mat1(filename)
        matriz2,tasks_per_machine = mat2(filename)
        matriz3,ordemlinhas = mat3(matriz1,matriz2,tasks_per_machine)
        matriz4,ordemcolunas = mat4(matriz3)
        
        
        print 'Matriz A'
        for i in matriz1:
        	print i
        print
        
        for i in xrange(len(tasks_per_machine)):
        	matriz2[i].append('|')
        	matriz2[i].append(tasks_per_machine[i])
        print "Matriz B"
        for i in matriz2:
        	print i
        print
        
        print ordemlinhas
        print
        
        print 'Matriz A com as linhas atualizadas'
        for i in matriz3:
        	print i
        print
        
        print ordemcolunas
        print
        
        print 'Matriz A Final'
        for i in matriz4:
        	print i
