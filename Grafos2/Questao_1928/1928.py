import heapq
class Solution:
    def minCost(self, maxTime: int, edges: list[list[int]], fees: list[int]) -> int:
        n = len(fees)  # Obtém o número total de cidades
        conexoes = [[] for _ in range(n)]  # Inicializa a lista de conexões entre cidades
        for origem, destino, duracao in edges:  # Adiciona as arestas ao grafo
            if duracao <= maxTime:  # Filtra as arestas com tempo válido
                conexoes[origem].append((destino, duracao))  
                conexoes[destino].append((origem, duracao)) 
        fila = [(fees[0], 0, 0)]  # Inicializa a fila com o custo do nó de origem 
        melhoresTempos = [float('inf')] * n  # Inicializa a lista de melhores tempos
        melhoresCustos = [float('inf')] * n  # Inicializa a lista de melhores custos
        melhoresTempos[0], melhoresCustos[0] = 0, fees[0]  # Configura o tempo e custo do nó inicial
        resultado = None  # Variável para armazenar o resultado final
        while fila:  
            custo, tempo, no = heapq.heappop(fila)  # Pega o nó com o menor custo da fila
            if no == n - 1:  # Verifica se chegou no destino final
                resultado = custo  # Define o resultado como o custo atual
                break  # Encerra o loop se o destino for alcançado
            if tempo > melhoresTempos[no] and custo >= melhoresCustos[no]:  # Verifica se o nó já foi visitado com melhores condições
                continue 
            melhoresTempos[no] = min(melhoresTempos[no], tempo)  
            melhoresCustos[no] = min(melhoresCustos[no], custo) 
            self.processarVizinhos(no, tempo, custo, conexoes, maxTime, fila, melhoresCustos, melhoresTempos, fees)  # Processa os vizinhos do nó atual
        if resultado is not None:  # Se um resultado válido foi encontrado
            return resultado  # Retorna o custo mínimo
        else:
            return -1  # Retorna -1 se não for possível alcançar o destino

    def processarVizinhos(self, no, tempo, custo, grafo, maxTime, fila, melhoresCustos, melhoresTempos, fees):
        def processarVizinho(vizinho, duracao): 
            novoTempo = tempo + duracao  # Calcula o novo tempo
            novoCusto = custo + fees[vizinho]  # Calcula o novo custo
            condicoes = {  # Dicionário para verificar as condições de tempo e custo
                "tempoValido": novoTempo <= maxTime,  # Verifica se o tempo é válido
                "custoValido": novoCusto < melhoresCustos[vizinho] or novoTempo < melhoresTempos[vizinho]  # Verifica se o custo ou tempo são válidos
            }
            if condicoes["tempoValido"] and condicoes["custoValido"]:  
                melhoresCustos[vizinho] = novoCusto  
                melhoresTempos[vizinho] = novoTempo  
                return novoCusto, novoTempo, vizinho  # Retorna o novo custo, tempo e o vizinho
            return None  
        for vizinho, duracao in grafo[no]:  # Para cada vizinho no grafo
            resultado = processarVizinho(vizinho, duracao)  # Processa o vizinho
            if resultado is not None:  # Se o vizinho passou nas condições
                heapq.heappush(fila, resultado)  # Adiciona à fila de prioridade
