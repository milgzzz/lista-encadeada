class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
    
    def esta_vazia(self):
        return self.tamanho == 0
    
    def obter_tamanho(self):
        return self.tamanho
    
    def obter_valor(self, posicao):
        if posicao < 1 or posicao > self.tamanho:
            raise IndexError(f"Posição inválida. A lista tem {self.tamanho} elementos.")
        
        atual = self.cabeca
        for _ in range(posicao - 1):
            atual = atual.proximo
        return atual.valor
    
    def modificar_valor(self, posicao, novo_valor):
        if posicao < 1 or posicao > self.tamanho:
            raise IndexError(f"Posição inválida. A lista tem {self.tamanho} elementos.")
        
        atual = self.cabeca
        for _ in range(posicao - 1):
            atual = atual.proximo
        atual.valor = novo_valor
    
    def inserir(self, posicao, valor):
        if posicao < 1 or posicao > self.tamanho + 1:
            raise IndexError(f"Posição inválida. Posições válidas: 1 a {self.tamanho + 1}.")
        
        novo_no = No(valor)
        
        if posicao == 1:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
        else:
            anterior = self.cabeca
            for _ in range(posicao - 2):
                anterior = anterior.proximo
            novo_no.proximo = anterior.proximo
            anterior.proximo = novo_no
        
        self.tamanho += 1
    
    def remover(self, posicao):
        if posicao < 1 or posicao > self.tamanho:
            raise IndexError(f"Posição inválida. A lista tem {self.tamanho} elementos.")
        
        if posicao == 1:
            removido = self.cabeca
            self.cabeca = removido.proximo
        else:
            anterior = self.cabeca
            for _ in range(posicao - 2):
                anterior = anterior.proximo
            removido = anterior.proximo
            anterior.proximo = removido.proximo
        
        self.tamanho -= 1
        return removido.valor
    
    def imprimir(self):
        atual = self.cabeca
        print("[", end=" ")
        while atual is not None:
            print(atual.valor, end=" ")
            atual = atual.proximo
        print("]")


def testar_lista_encadeada():
    print("\n= TESTE DA LISTA ENCADEADA =")
    
    lista = ListaEncadeada()
    print("\n1. Lista criada:")
    lista.imprimir()  
    print("Lista vazia?", lista.esta_vazia())  
    print("Tamanho:", lista.obter_tamanho())  
    
    print("\n2. Inserindo elementos:")
    
    lista.inserir(1, 10)
    lista.inserir(2, 20)  
    lista.inserir(3, 30)  
    lista.inserir(1, 5)   
    lista.inserir(3, 15)  
    lista.imprimir()  
    
    print("Tamanho:", lista.obter_tamanho())  
    
    print("\n3. Acesso e modificação:")
    print("Elemento na posição 2:", lista.obter_valor(2))  
    print("Elemento na posição 4:", lista.obter_valor(4))  
    
    lista.modificar_valor(3, 100)
    print("Após modificar posição 3 para 100:")
    lista.imprimir()  
    
    print("\n4. Remoção de elementos:")
    removido = lista.remover(2)
    print(f"Removido da posição 2: {removido}")
    lista.imprimir()  
    
    removido = lista.remover(1)
    print(f"Removido da posição 1: {removido}")
    lista.imprimir()  
    
    removido = lista.remover(3)
    print(f"Removido da posição 3: {removido}")
    lista.imprimir() 
    
    print("Tamanho atual:", lista.obter_tamanho())  # 2
    
    print("\n5. Teste de erros:")
    
    try:
        lista.obter_valor(0) 
    
    except IndexError as e:
        print("Erro ao acessar posição 0:", e)
    
    try:
        lista.inserir(5, 99)  
    
    except IndexError as e:
        print("Erro ao inserir na posição 5:", e)
    
    try:
        lista.remover(3)  
    
    except IndexError as e:
        print("Erro ao remover posição 3:", e)
    
    print("\n6. Esvaziando a lista:")
    
    lista.remover(1)
    lista.remover(1)
    lista.imprimir() 
    
    print("Lista vazia?", lista.esta_vazia())  
    print("Tamanho:", lista.obter_tamanho())  

if __name__ == "__main__":
    testar_lista_encadeada()