#Bibliotecas.
import nltk 
from nltk.chat.util import Chat, reflections 
from tkinter import * 

#Respostas esperadas pelo Chat, com cada número respectivamente colocado para as respostas.
patterns = [
    (r'1', ['R: GTA RP (Roleplay) é um modo de jogo no GTA V em que os jogadores interpretam personagens com histórias, profissões e regras, como se fosse uma vida real dentro do jogo.']),
    (r'2', ['R: Sim, é obrigatório ter o GTA V original na Steam, Epic Games ou Rockstar Launcher para jogar GTA RP.']),
    (r'3', ['R: A maioria dos servidores usa o FiveM, uma plataforma que permite jogar GTA RP com mods e servidores personalizados.']),
    (r'4', ['R: Você precisa instalar o FiveM, encontrar um servidor (via lista ou Discord), seguir as regras dele e passar pelo processo de whitelist (alguns têm entrevista ou formulário).']),
    (r'5', ['R: Whitelist é um processo de aprovação para garantir que os jogadores entendem as regras de RP. Pode envolver entrevista, formulário ou até testes dentro do jogo.']),
    (r'6', ['R: Sim, desde que siga as regras do servidor. Você pode ser policial, mecânico, criminoso, médico, empresário e muito mais, dependendo da proposta do servidor.']),
    (r'7', ['R: Power gaming: Forçar ações sem dar chance ao outro jogador (ex: “te amarrei e te joguei no carro” sem rolagem). Metagaming: Usar informações de fora do jogo (ex: Discord, live) como se seu personagem soubesse.']),
    (r'8', ['R: Sim, o Five M é gratuito. Mas alguns servidores cobram por acesso premium, skins exclusivas ou prioridade na fila.']),
    (r'9', ['R: Agradeço, E que bom que consegui esclarecer tudo.👍'])
] 

FIVeM = Chat(patterns, reflections) 

#Colocando resposta para o usuário, e a forma do usuário sair.
def speak(): 
  escolha_usuario = entry.get() 
  if escolha_usuario.lower() == "9": 
    chat_log.insert(END, "FIVeM: Até logo.👌 ") 
    janela.quit() 

    #Caso usuário escolha não sair, o Chat continuará respondendo.
  else:
    resposta = FIVeM.respond(escolha_usuario) 
    chat_log.insert(END, f"Você: {escolha_usuario}\n") 
    chat_log.insert(END, f"FIVeM: {resposta}\n") 
    entry.delete(0, END) 

#Tela de Boas-Vindas e todas as perguntas que podem ser feitas.
def interação_com_usuario(): 
  chat_log.insert(END, "FIVeM: Olá. Me chamo FIVeM e estou aqui para ajudar. Digite o número da pergunta que deseja saber:😊\n")
  chat_log.insert(END, "1 - O que é GTA RP?\n")
  chat_log.insert(END, "2 - Preciso ter o GTA V original para jogar?\n")
  chat_log.insert(END, "3 - Qual programa eu uso para jogar?\n")
  chat_log.insert(END, "4 - Como entrar em um servidor?\n")
  chat_log.insert(END, "5 - O que é whitelist?\n")
  chat_log.insert(END, "6 - Posso ser qualquer personagem?\n")
  chat_log.insert(END, "7 - O que é power gaming e metagaming?\n")
  chat_log.insert(END, "8 - GTA RP é gratuito?\n")
  chat_log.insert(END, "9 - Sair😘\n")

#Janela da biblioteca Tkinter
janela = Tk() 
janela.title("FIVeM") 

#Definindo tamanho da janela.
chat_log = Text(janela, height=30, width=100)
chat_log.pack() 


entry = Entry(janela, width=100)
entry.pack() 

#Botão de envio de mensagem para o Chat.
send_button = Button(janela, text="Enviar", command=speak)
send_button.pack() 

interação_com_usuario()

#Loop para janela continuar aberta até que o usuário escolha sair. 
janela.mainloop()
