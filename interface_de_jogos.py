from random import choice,randint
from os import system
from time import sleep
from sys import exit
import tkinter as tk  

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
# | Configuração do Botão que aciona a funcionalidade Calculadora		        |
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

def botao_calculadora():

#
#				=====================================================================
# 				| 	CONFIGURAÇÃO DA JANELA DA CALCULADORA	       			 		|
# 				=====================================================================
#
#
	def janela_calculadora():
		janela_calculadora = tk.Toplevel(menu)
		janela_calculadora.title("Calculadora")
		janela_calculadora.geometry("650x400")
		informacao_janela_calculadora = tk.Label(janela_calculadora, text="Aperte na operação matemática desejada:", font = ("Arial", 18, "bold"))
		informacao_janela_calculadora.pack()
		botao_soma = tk.Button(janela_calculadora, text="SOMA", command=janela_calculadora_soma)
		botao_subtração = tk.Button(janela_calculadora, text="SUBTRAÇÃO", command=janela_calculadora_subtração)
		botao_divisão = tk.Button(janela_calculadora, text="DIVISÃO", command=janela_calculadora_divisão)
		botao_multiplicação = tk.Button(janela_calculadora, text="MULTIPLICAÇÃO", command=janela_calculadora_multiplicação)
		botao_soma.pack()
		botao_subtração.pack()
		botao_divisão.pack()
		botao_multiplicação.pack()
#
#				=====================================================================
# 				| 	CONFIGURAÇÃO DA PARTE RESPONSÁVEL PELA SOMA	        			|
# 				=====================================================================
#
#
	#  ------------ Configuração da Janela da SOMA ------------	
	def janela_calculadora_soma():
		janela_soma = tk.Toplevel()
		janela_soma.title("Soma")
		janela_soma.geometry("400x250")
		informacao_janela_soma = tk.Label(janela_soma, text="Calcule a SOMA de DOIS números:")
		informacao_janela_soma.pack()
		numero_um_entrada = tk.Entry(janela_soma)
		simbolo_soma = tk.Label(janela_soma, text="+")
		numero_dois_entrada = tk.Entry(janela_soma)
		simbolo_igual = tk.Label(janela_soma, text="=")
		numero_um_entrada.pack()
		simbolo_soma.pack()
		numero_dois_entrada.pack()

	#  ------------ A parte da SOMA em si e resultado ------------
		resultado_soma = tk.Label(janela_soma)
		def obter_numero_e_somar():
			try:
				numero_um = float(numero_um_entrada.get())
				numero_dois = float(numero_dois_entrada.get())
				resultado = numero_um + numero_dois
				resultado_soma["text"]= f"Resultado: [{resultado}]"
				resultado_soma.pack()
			except ValueError:
				resultado_soma["text"] = "Entrada inválida!"
				resultado_soma.pack()
		def mostrar_resultado_soma():
			janela_soma.after(250, obter_numero_e_somar)
			resultado_soma.pack()

	#  ------------ Configuração da Janela da SOMA ------------	
		botao_calcular = tk.Button(janela_soma, text="CALCULAR", command= mostrar_resultado_soma)
		botao_calcular.pack()
		simbolo_igual.pack()
#
#				=====================================================================
# 				| 	CONFIGURAÇÃO DA PARTE RESPONSÁVEL PELA SUBTRAÇÃO	        	|
# 				=====================================================================
#
#
	#  ------------ Configuração da Janela da SUBTRAÇÃO ------------
	def janela_calculadora_subtração():
		janela_subtração = tk.Toplevel()
		janela_subtração.title("Subtração")
		janela_subtração.geometry("400x250")
		informacao_janela_subtração = tk.Label(janela_subtração, text="Calcule a SUBTRAÇÃO de DOIS números:")
		informacao_janela_subtração.pack()
		numero_um_entrada = tk.Entry(janela_subtração)
		simbolo_subtração = tk.Label(janela_subtração, text="-")
		numero_dois_entrada = tk.Entry(janela_subtração)
		simbolo_igual = tk.Label(janela_subtração, text="=")
		numero_um_entrada.pack()
		simbolo_subtração.pack()
		numero_dois_entrada.pack()

	#  ------------ A parte da SUBTRAÇÃO em si e resultado ------------
		resultado_subtração = tk.Label(janela_subtração)
		def obter_numero_e_subtrair():
			try:
				numero_um = float(numero_um_entrada.get())
				numero_dois = float(numero_dois_entrada.get())
				resultado = numero_um - numero_dois
				resultado_subtração["text"]= f"Resultado: [{resultado}]"
				resultado_subtração.pack()
			except ValueError:
				resultado_subtração["text"] = "Entrada inválida!"
				resultado_subtração.pack()
		def mostrar_resultado_subtração():
			janela_subtração.after(250, obter_numero_e_subtrair)
			resultado_subtração.pack()

	#  ------------ Configuração da Janela da SUBTRAÇÃO ------------	
		botao_calcular = tk.Button(janela_subtração, text="CALCULAR", command= mostrar_resultado_subtração)
		botao_calcular.pack()
		simbolo_igual.pack()
#
#				=====================================================================
# 				| 	CONFIGURAÇÃO DA PARTE RESPONSÁVEL PELA DIVISÃO	        		|
# 				=====================================================================
#
#		
	#  ------------ Configuração da Janela da DIVISÃO ------------
	def janela_calculadora_divisão():
		janela_divisão = tk.Toplevel()
		janela_divisão.title("Divisão")
		janela_divisão.geometry("400x250")
		informacao_janela_divisão = tk.Label(janela_divisão, text="Calcule a DIVISÃO de DOIS números:")
		informacao_janela_divisão.pack()	
		numero_um_entrada = tk.Entry(janela_divisão)
		simbolo_divisão = tk.Label(janela_divisão, text="÷")
		numero_dois_entrada = tk.Entry(janela_divisão)
		simbolo_igual = tk.Label(janela_divisão, text="=")
		numero_um_entrada.pack()
		simbolo_divisão.pack()
		numero_dois_entrada.pack()

	#  ------------ A parte da DIVISÃO em si e resultado ------------
		resultado_divisão = tk.Label(janela_divisão)
		def obter_numero_e_dividir():
			try:
				numero_um = float(numero_um_entrada.get())
				numero_dois = float(numero_dois_entrada.get())
				resultado = numero_um / numero_dois
				resultado_divisão["text"]= f"Resultado: [{resultado}]"
				resultado_divisão.pack()
			except ValueError:
				resultado_divisão["text"] = "Entrada inválida!"
				resultado_divisão.pack()
		def mostrar_resultado_divisão():
			janela_divisão.after(250, obter_numero_e_dividir)
			resultado_divisão.pack()

	#  ------------ Configuração da Janela da DIVISÃO ------------		
		botao_calcular = tk.Button(janela_divisão, text="CALCULAR", command= mostrar_resultado_divisão)
		botao_calcular.pack()
		simbolo_igual.pack()
#
#				=====================================================================
# 				| 	CONFIGURAÇÃO DA PARTE RESPONSÁVEL PELA MULTIPLICAÇÃO	        |
# 				=====================================================================
#
#
	#  ------------ Configuração da Janela da MULTIPLICAÇÃO ------------
	def janela_calculadora_multiplicação():
		janela_multiplicação = tk.Toplevel()
		janela_multiplicação.title("Multiplicação")
		janela_multiplicação.geometry("400x250")
		informacao_janela_multiplicação = tk.Label(janela_multiplicação, text="Calcule a MULTIPLICAÇÃO de DOIS números:")
		informacao_janela_multiplicação.pack()
		numero_um_entrada = tk.Entry(janela_multiplicação)
		simbolo_multiplicação = tk.Label(janela_multiplicação, text="X")
		numero_dois_entrada = tk.Entry(janela_multiplicação)
		simbolo_igual = tk.Label(janela_multiplicação, text="=")
		numero_um_entrada.pack()
		simbolo_multiplicação.pack()
		numero_dois_entrada.pack()

	#  ------------ A parte da MULTIPLICAÇÃO em si e resultado ------------
		resultado_multiplicação = tk.Label(janela_multiplicação)
		def obter_numero_e_multiplicar():
			try:
				numero_um = float(numero_um_entrada.get())
				numero_dois = float(numero_dois_entrada.get())
				resultado = numero_um * numero_dois
				resultado_multiplicação["text"]= f"Resultado: [{resultado}]"
				resultado_multiplicação.pack()
			except ValueError:
				resultado_multiplicação["text"] = "Entrada inválida!"
				resultado_multiplicação.pack()
		def mostrar_resultado_multiplicação():
			janela_multiplicação.after(250, obter_numero_e_multiplicar)
			resultado_multiplicação.pack()

	#  ------------ Configuração da Janela da MULTIPLICAÇÃO ------------
		botao_calcular = tk.Button(janela_multiplicação, text="CALCULAR", command= mostrar_resultado_multiplicação)
		botao_calcular.pack()
		simbolo_igual.pack()

	janela_calculadora()    

	
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
# | Configuração do Botão que aciona a funcionalidade do Pedra, Papel e Tesoura |
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

def botao_pedra_papel_e_tesoura():

	# Sistema de pontuação e iniciação de variável
	opcoes = ["Pedra", "Papel", "Tesoura"]
	escolha_maquina = choice(opcoes)
	ponto_jogador = 0
	ponto_maquina = 0
	escolha_maquina = None
	escolha_jogador = None    	

	def Pedra():
		global escolha_jogador
		escolha_jogador = "Pedra"
		global ganhador_rodada, ponto_jogador, ponto_maquina
		if escolha_maquina == "Papel":
			ganhador_rodada = "O campeão da rodada é a Máquina"
			ponto_maquina+=1
		elif escolha_maquina == "Tesoura":
			ganhador_rodada = "O campeão da rodada é o Jogador"
			ponto_jogador+=1
		elif escolha_maquina == "Pedra":
			ganhador_rodada = "A rodada é empate ja que ambos escolheram a mesma coisa"

	def Papel():
		global escolha_jogador
		escolha_jogador = "Papel"
		global ganhador_rodada, ponto_jogador, ponto_maquina
		if escolha_maquina == "Tesoura":
			ganhador_rodada = "O campeão da rodada é a Máquina"
			ponto_maquina+=1
		elif escolha_maquina == "Pedra":
			ganhador_rodada = "O campeão da rodada é o Jogador"
			ponto_jogador+=1
		elif escolha_maquina == "Papel":
			ganhador_rodada = "A rodada é empate ja que ambos escolheram a mesma coisa"			

	def Tesoura():
		global escolha_jogador
		escolha_jogador = "Tesoura"
		global ganhador_rodada, ponto_jogador, ponto_maquina
		if escolha_maquina == "Pedra":
			ganhador_rodada = "O campeão da rodada é a Máquina"
			ponto_maquina+=1
		elif escolha_maquina == "Papel":
			ganhador_rodada = "O campeão da rodada é o Jogador"
			ponto_jogador+=1
		elif escolha_maquina == "Tesoura":
			ganhador_rodada = "A rodada é empate ja que ambos escolheram a mesma coisa"				

	def janela_pedra_papel_e_tesoura():
		janela_pedra_papel_e_tesoura = tk.Toplevel(menu)
		janela_pedra_papel_e_tesoura.title("Pedra Papel e Tesoura")
		janela_pedra_papel_e_tesoura.geometry("700x600")
		informacao_janela_pedra_papel_e_tesoura= tk.Label(janela_pedra_papel_e_tesoura, text="Faça 10 pontos e ganhe da Máquina", font = ("Arial", 14, "bold"))
		informacao_janela_pedra_papel_e_tesoura.pack()
		# Configuração da Janela
		ponto_jogador_janela = tk.Label(janela_pedra_papel_e_tesoura, text=ponto_jogador)
		ponto_jogador_janela.pack()
		botao_Pedra = tk.Button(janela_pedra_papel_e_tesoura, text="Pedra", command=Pedra)
		botao_Papel = tk.Button(janela_pedra_papel_e_tesoura, text="Papel", command=Papel)
		botao_Tesoura = tk.Button(janela_pedra_papel_e_tesoura, text="Tesoura", command=Tesoura)
		print_escolha_jogador = tk.Label(janela_pedra_papel_e_tesoura, text=f"A escolha do jogador é {escolha_jogador}")
		print_escolha_jogador.pack()
		botao_Pedra.pack()
		botao_Papel.pack()
		botao_Tesoura.pack()

	janela_pedra_papel_e_tesoura()

	system("clear")
	def quer_continuar():
		resposta = input("[!] Pressione ENTER para permanecer jogando ou digite SAIR para parar de jogar> ").lower()
		if resposta == "sair":
			print("[!] Foi um prazer jogar com você!")
			exit()
		else:
			system("clear")

	def checar_vitoria(pontos_jogador, pontos_maquina):
		vencedor = None
		if pontos_jogador == 10:
			vencedor = "JOGADOR"
		if pontos_maquina == 10:
			vencedor = "COMPUTADOR"
		if vencedor is not None:
			system("clear")
			print(f"[~] A pontuação final foi {pontos_jogador} PONTOS jogador e {pontos_maquina} PONTOS maquina")
			print(f"[+] O {vencedor} é o GRANDE VENCEDOR!!!!!!")
			exit()
		else:
			quer_continuar()

	def jogar_pedra_papel_tesoura():
		print("** Vamos jogar Pedra, Papel ou Tesoura :D **")
		print("--!-- Ganha quem alcançar 10 pontos primeiro ou pedir pra sair. QUE VENÇA O MELHOR --!--")
		opcoes = ["pedra", "papel", "tesoura"]
		parar = ""
		ponto_maquina = 0
		ponto_jogador = 0
		while parar != "sair":
			escolha = ""
			print(f"A pontuação atual é {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
			while escolha not in opcoes:
				escolha = input("[+] Você vai escolher Pedra, Papel ou Tesoura? ").lower()
				if escolha not in opcoes:
					print("[!] Você precisa colocar uma opção válida")
			print("[!] Vou fazer uma escolha *BIP* *BOP*....")
			sleep(1)
			escolha_maquina = choice(opcoes)

			# ----  ---- Condições de EMPATE ----  ----
			if escolha_maquina == escolha:
				print("[!] Escolhemos a mesma coisa")
				print("[~] Essa rodada foi empate")
				ponto_maquina += 1
				ponto_jogador += 1
				checar_vitoria(ponto_jogador, ponto_maquina)

			#  ----  ---- Condições de Vitória de Jogador ----  ----
			elif escolha == "tesoura" and escolha_maquina == "papel":
				print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
				print("[~] Você ganhou essa rodada")
				ponto_jogador += 1
				checar_vitoria(ponto_jogador, ponto_maquina)
			elif escolha == "papel" and escolha_maquina == "pedra":
				print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
				print("[~] Você ganhou essa rodada")
				ponto_jogador += 1
				checar_vitoria(ponto_jogador, ponto_maquina)
			elif escolha == "pedra" and escolha_maquina == "tesoura":
				print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
				print("[~] Você ganhou essa rodada")
				ponto_jogador += 1
				checar_vitoria(ponto_jogador, ponto_maquina)

			#  ----  ---- Condições de Derrota do Jogador ----  ----
			elif escolha_maquina == "tesoura" and escolha == "papel":
				print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
				print("[~] Você perdeu essa rodada")
				ponto_maquina += 1
				checar_vitoria(ponto_jogador, ponto_maquina)
			elif escolha_maquina == "papel" and escolha == "pedra":
				print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
				print("[~] Você perdeu essa rodada!")
				ponto_maquina += 1
				checar_vitoria(ponto_jogador, ponto_maquina)
			elif escolha_maquina == "pedra" and escolha == "tesoura":
				print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
				print("[~] Você perdeu essa rodada")
				ponto_maquina += 1
				checar_vitoria(ponto_jogador, ponto_maquina)
			else:
				print("[!] Algo deu errado!")
				break

	if __name__ == "__main__":
		jogar_pedra_papel_tesoura()

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
# | Configuração do Botão que aciona a funcionalidade Adivinha Número           |
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----	    

def botao_adivinha_numero():
		system("clear")
		nome = input("[+] Me diga o seu nome> ")
		print("Me diga um começo e fim inteiro e eu irei escolher um número pra você tentar adivinhar")
		while True:
			inicio = int(input("Me diga o número de inicio> "))
			fim = int(input("Me diga o número de fim> "))
			if fim < inicio:
				print("[!] O número escolhido para ser fim não pode ser menor que o de inicio")
			elif fim == inicio or inicio == fim:
				print("[!] Os números escolhidos para fim e inicio não podem ser iguais")
			elif (fim-inicio)==1:
				print("[!] É preciso que exista pelo menos 1 numero inteiro entre o inicio e fim")
			else:
				break
		numero_computador = randint(inicio,fim)
		count = 0
		tentativas = []
		while True:
			if numero_computador == fim or numero_computador == inicio:
				numero_computador = randint(inicio,fim)
			else:
				break
		while True:
			numero_jogador=int(input("[+] Me diga o seu numero> "))
			if numero_jogador > numero_computador and numero_jogador < fim:
				count+=1
				print("[!] O número que pensei é menor")
				tentativas.append(numero_jogador)
			elif numero_jogador < numero_computador and numero_jogador > inicio:
				count+=1
				print("[!] O número que pensei é maior")
				tentativas.append(numero_jogador)
			elif numero_jogador > fim:
				count+=1
				print("[!] Você precisa colocar um numero menor que o seu fim")
				tentativas.append(numero_jogador)
			elif numero_jogador < inicio:
				count+=1
				print("[!] Você precisa colocar um numero menor que o seu inicio")
				tentativas.append(numero_jogador)
			elif numero_jogador == numero_computador:
				count+=1
				print(f"Parabéns {nome} o seu numero de tentativas foi {count}!!")
				tentativas.append(numero_jogador)
				print(f"Suas tentativas foram = {tentativas}")
				break
			elif numero_jogador == inicio or numero_jogador == fim:
				count+=1
				print("[!] Coloque um valor inteiro dentro do limite estabelecido por você")
				tentativas.append(numero_jogador)

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
# | 						Configurações da Interface        					 |
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----	

# Parte Visual e integrações 
menu = tk.Tk()
menu.title("Interface de Jogos")
menu.geometry("650x400")
titulo_menu = tk.Label(menu, text="Seja bem-vindo à interface de jogos de Ske1337on", font = ("Arial", 18, "bold"))
informacoes_menu = tk.Label(menu, text = "Para mais códigos: https://github.com/Ske1337on\n"
											"Você poderá escolher entre as opções abaixo:", font = ("Times New Roman", 12))
titulo_menu.pack()
informacoes_menu.pack()

# Parte interativa e integrações 
botao_calculadora = tk.Button(menu, text="Calculadora", command=botao_calculadora)
botao_pedra_papel_e_tesoura = tk.Button(menu, text="Pedra, Papel e Tesoura", command=botao_pedra_papel_e_tesoura)
botao_adivinha_numero = tk.Button(menu, text = "Adivinhador de Número", command = botao_adivinha_numero)
botao_calculadora.pack()
botao_pedra_papel_e_tesoura.pack()
botao_adivinha_numero.pack()

# Inicia o loop principal da janela
menu.mainloop()

