import pygame
from scripts.cano import Cone
from scripts.jogador import Jogador
from scripts.interfaces import Texto
from scripts.interfaces import Botao

class Partida:

    def __init__(self, tela):
        self.tela = tela
        self.fundo = pygame.image.load("assets/fundo.png")
        self.fundo = pygame.transform.scale(self.fundo, self.tela.get_size())
        self.jogador = Jogador(tela, 300, 300)

        # Criar vários cones
        self.cones = [Cone(tela) for _ in range(5)]

        self.estado = "partida"

        self.pontosValor = 0
        self.contador = 0
        self.pontosTexto = Texto(tela,str(self.pontosValor),10,10,(255,255,255),30)
    
    def atualizar(self):
        self.tela.blit(self.fundo, (0, 0))
        self.estado = "partida"
        self.jogador.atualizar()

        # Atualizar cones
        for cone in self.cones:
            cone.atualizar()

        # Pontos
        self.contador += 1
        if self.contador > 60:
            self.pontosValor += 1
            self.contador = 0
            self.pontosTexto.atualizarTexto(str(self.pontosValor))
        
        self.pontosTexto.desenhar()

        # Detectar colisão com qualquer cone
        for cone in self.cones:
            if cone.detectarColisao(self.jogador.getRect()):
                self.estado = "menu"
                self.jogador.posicao = (100,100)

                # Resetar cones
                self.cones = [Cone(self.tela) for _ in range(5)]
                break

        # Desenhar jogador
        self.jogador.desenhar()

        # Desenhar cones
        for cone in self.cones:
            cone.desenhar()

        return self.estado

class Menu:

    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela,"FlappyBird", 100, 20,(255,255,255),50)
        self.estado = "menu"
        self.botao_jogar = Botao(tela,"Jogar",100,100,50,(200,0,0),(255,255,255))

    def atualizar(self):
        self.estado = "menu" 
        self.titulo.desenhar()
        self.botao_jogar.desenhar()

        if self.botao_jogar.get_click():
            self.estado = "partida"
        
        return self.estado