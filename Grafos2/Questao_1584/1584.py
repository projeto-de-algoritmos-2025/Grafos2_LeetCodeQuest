import heapq
from collections import defaultdict
class Solution(object):
    def calcular_distancias(self, points):  
        total_pontos = len(points)  
        grafo = defaultdict(list)  # Dicionário para armazenar as distâncias entre os pontos
        x = 0
        while x < total_pontos:  # Loop para percorrer todos os pontos
            y = x + 1
            while y < total_pontos:  # Loop para comparar os pontos
                distancia = abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])  # Calcula a distância de Manhattan entre os pontos
                grafo[x].append((distancia, y))  # Adiciona a aresta no grafo (x, y)
                grafo[y].append((distancia, x))  # Adiciona a aresta no grafo (y, x)
                y += 1
            x += 1
        return grafo  # Retorna o grafo com as distâncias
    def minCostConnectPoints(self, points):  
        total_pontos = len(points)  # Obtém o número total de pontos
        visitado = [0] * total_pontos  # Inicializa a lista de visitados com 0 (Não visitado)
        custo_total = 0  # Inicializa o custo total com 0
        visitados = 1  # Inicializa o contador de pontos visitados com 1 (O ponto 0 é visitado inicialmente)
        visitado[0] = 1  # Marca o ponto 0 como visitado
        grafo = self.calcular_distancias(points)  # Chama a função para calcular as distâncias e obter o grafo
        fila = grafo[0][:]  # Cria uma cópia da lista de vizinhos de 0
        heapq.heapify(fila)  # Converte a lista em uma heap 
        while visitados < total_pontos:  # Enquanto todos os pontos forem visitados
            custo, proximo = heapq.heappop(fila)  # Pega o ponto de menor custo da fila
            if visitado[proximo] == 0:  # Verifica se o ponto ainda não foi visitado
                visitado[proximo] = 1  # Marca o ponto como visitado
                custo_total += custo  # Adiciona o custo da aresta ao custo total
                visitados += 1  # Incrementa o contador de pontos visitados
                for vizinho_custo, vizinho in grafo[proximo]:  # Itera sobre os vizinhos
                    if visitado[vizinho] == 0:  # Verifica se o vizinho ainda não foi visitado
                        heapq.heappush(fila, (vizinho_custo, vizinho))  # Adiciona o vizinho à fila
        return custo_total  # Retorna o custo total para conectar todos os pontos
