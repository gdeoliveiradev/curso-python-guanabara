# Faça um programa em python que abra e reproduza o audio de um arquivo mp3

# Importando biblioteca para o projeto
import pygame

# Iniciando sistema de audio
pygame.mixer.init()

# Caminho do audio
CAMINHO_AUDIO = 'F:/TI/Estudos/Python/curso-em-video/mundo1/PythonDesafios/hino.mp3'

# Carregando e reproduzindo
pygame.mixer.music.load(CAMINHO_AUDIO)
pygame.mixer.music.play()

# Mantem o programa rodando até o audio terminar
input('Pressione ENTER para parar...')
