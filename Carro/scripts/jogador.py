import pygame

class Jogador:  
    def __init__(self, tela, x, y):  
        
        self.posicao = [x, y]  
        self.tamanho = [32, 32]  
        self.rect = pygame.Rect(self.posicao, self.tamanho)  

        self.contador = 0  
        self.imagemAtual = 0  
        self.tela = tela 
        self.listaImagens = []  

        for i in range(3):  
            imagem = pygame.image.load(f'assets/carro.png')
            
            imagem = pygame.transform.scale(imagem, self.tamanho)
            
            self.listaImagens.append(imagem)
            
        self.velocidadeAtual = 0
        self.velocidadeBarra = 1/60 * 10
        self.velocidadeMaxima = 1/60 * 100

    def desenhar(self):
        self.contador += 1
        if self.contador > 5:
            self.contador = 0
            self.imagemAtual = (self.imagemAtual + 1) % 3
        self.tela.blit(self.listaImagens[self.imagemAtual], self.posicao)

    def atualizar(self):
    # Gravidade / velocidade vertical
        self.velocidadeAtual = min(self.velocidadeAtual, self.velocidadeMaxima)
        self.posicao[1] += self.velocidadeAtual

        # Atualiza o rect
        self.rect = pygame.Rect(self.posicao, self.tamanho)

        # Movimentação horizontal
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_a]:  # Esquerda
            self.posicao[0] -= 5  

        if teclas[pygame.K_d]:  # Direita
            self.posicao[0] += 5

    def getRect(self):
        return pygame.Rect(self.posicao,self.tamanho)
    