import pygame
import random 

class Cone:
    def __init__(self, tela):
        self.imagem = pygame.image.load('assets/cone.png') 
        self.tela = tela 
        
        # Posição inicial (lá em cima)
        self.y = -self.imagem.get_height()
        self.velocidade = 3

        # Posição horizontal aleatória
        self.x = random.randint(50, tela.get_width() - 50)


        # Calcula posições
        self.atualizarPosicoes()

    def atualizarPosicoes(self):
        # Cone esquerdo
        self.cone = (self.x, self.y)


    def atualizar(self):
        # Cones descem
        self.y += self.velocidade

        # Se saiu da tela, reposiciona
        if self.y > self.tela.get_height():
            self.y = -self.imagem.get_height()
            self.x = random.randint(50, self.tela.get_width() - 50)
        
        self.atualizarPosicoes()

    def desenhar(self):
        # Cones caindo
        self.tela.blit(self.imagem, self.cone)

    def detectarColisao(self, rectJogador):
        rectCone = pygame.Rect(self.cone, self.imagem.get_size())
        return rectJogador.colliderect(rectCone)
