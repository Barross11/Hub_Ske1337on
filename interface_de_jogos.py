from random import choice,randint
import tkinter as tk 
from tkinter import messagebox 

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
	global ponto_jogador
	global ponto_maquina
	global escolha_maquina
	global escolha_jogador
	global ganhador_rodada	
	ponto_jogador=0
	ponto_maquina=0
	escolha_maquina = ""
	escolha_jogador = "" 
	ganhador_rodada = ""

	def fim_De_jogo():
		global ponto_maquina
		global ponto_jogador
		global ganhador_rodada
		if ponto_jogador == 10 or ponto_maquina == 10:
			messagebox.showinfo("PARÁBENS", f"{ganhador_rodada} é o grande CAMPEÃO")
			ponto_jogador=0
			ponto_maquina=0
			ganhador_rodada = ""
			limpar_escolhas()



	def atualizar_escolhas():
		global print_escolha_maquina
		global print_escolha_jogador
		global escolha_jogador
		global escolha_maquina
		print_escolha_jogador.config(text=f"A escolha do Jogador é {escolha_jogador}")
		print_escolha_maquina.config(text=f"A escolha da Máquina é {escolha_maquina}") 
		condições_de_vitoria()

	def maquina_escolhendo():
		global escolha_maquina
		escolha_maquina = choice(opcoes)
		atualizar_escolhas()		

	def limpar_escolhas():
		global escolha_jogador
		global escolha_maquina		
		escolha_jogador = "" 
		escolha_maquina = ""

	def placar():
		global ganhador_rodada
		global ponto_jogador
		global ponto_maquina
		global placar_1
		global mensagem_de_Campeão		
		if ganhador_rodada == "Jogador":
			ponto_jogador+=1
			mensagem_de_Campeão.config(text=f"O grande vencedor é {ganhador_rodada} ", font = ("Arial", 11, "bold"))
			fim_De_jogo()
		elif ganhador_rodada == "Máquina":
			ponto_maquina+=1
			mensagem_de_Campeão.config(text=f"O grande vencedor é {ganhador_rodada} ", font = ("Arial", 11, "bold"))
			fim_De_jogo()
		elif ganhador_rodada == "Ninguém, foi EMPATE":
			mensagem_de_Campeão.config(text=f"O grande vencedor é {ganhador_rodada} ", font = ("Arial", 11, "bold"))
		placar_1.config(text=f"O placar atual é {ponto_jogador} PONTOS JOGADOR e {ponto_maquina} PONTOS MÁQUINA")
		limpar_escolhas()

	def condições_de_vitoria():
		global ponto_jogador
		global ponto_maquina
		global escolha_jogador
		global escolha_maquina
		global ganhador_rodada				
		if (escolha_jogador == "Pedra" and escolha_maquina == "Tesoura") or (escolha_jogador == "Papel" and escolha_maquina == "Pedra") or (escolha_jogador == "Tesoura" and escolha_maquina == "Papel"):
			ganhador_rodada = "Jogador"
			placar()
		elif (escolha_jogador == "Tesoura" and escolha_maquina == "Pedra") or (escolha_jogador == "Pedra" and escolha_maquina == "Papel") or (escolha_jogador == "Papel" and escolha_maquina == "Tesoura"):
			ganhador_rodada = "Máquina"
			placar()
		elif escolha_jogador == escolha_maquina:
			ganhador_rodada = "Ninguém, foi EMPATE"
			placar()			

	def Pedra():
		global escolha_jogador
		escolha_jogador = "Pedra"
		maquina_escolhendo()		

	def Papel():
		global escolha_jogador		
		escolha_jogador = "Papel"
		maquina_escolhendo()
				
	def Tesoura():
		global escolha_jogador
		escolha_jogador = "Tesoura"
		maquina_escolhendo()

	def func_pedra_papel_e_tesoura():
		global placar_1
		global mensagem_de_Campeão
		global print_escolha_jogador
		global print_escolha_maquina
		global janela_pedra_papel_e_tesoura
		global ponto_jogador
		global ponto_maquina
		global escolha_maquina
		global escolha_jogador
		global ganhador_rodada	
		janela_pedra_papel_e_tesoura = tk.Toplevel(menu)
		janela_pedra_papel_e_tesoura.title("Pedra Papel e Tesoura")
		janela_pedra_papel_e_tesoura.geometry("560x160")
		informacao_janela_pedra_papel_e_tesoura= tk.Label(janela_pedra_papel_e_tesoura, text="Faça 10 pontos e ganhe da Máquina", font = ("Arial", 14, "bold"))
		informacao_janela_pedra_papel_e_tesoura.grid(row=0, column=1)
		# Configuração da Janela
		botao_Pedra = tk.Button(janela_pedra_papel_e_tesoura, text="Pedra", command=Pedra)
		botao_Papel = tk.Button(janela_pedra_papel_e_tesoura, text="Papel", command=Papel)
		botao_Tesoura = tk.Button(janela_pedra_papel_e_tesoura, text="Tesoura", command=Tesoura)
		print_escolha_jogador = tk.Label(janela_pedra_papel_e_tesoura, text=f"A escolha do Jogador é {escolha_jogador}")
		print_escolha_maquina = tk.Label(janela_pedra_papel_e_tesoura, text=f"A escolha da Máquina é {escolha_maquina}")
		print_escolha_jogador.grid(row=2, column=1)
		print_escolha_maquina.grid(row=3, column=1)		
		placar_1 = tk.Label(janela_pedra_papel_e_tesoura, text=f"O placar atual é {ponto_jogador} PONTOS JOGADOR e {ponto_maquina} PONTOS MÁQUINA")
		placar_1.grid(row=1, column=1)		
		mensagem_de_Campeão= tk.Label(janela_pedra_papel_e_tesoura, text=f"O grande vencedor é {ganhador_rodada} ", font = ("Arial", 11, "bold"))
		mensagem_de_Campeão.grid(row=4, column=1)
		botao_Pedra.grid(row=6, column=0, padx=10)
		botao_Papel.grid(row=6, column=1, padx=10)
		botao_Tesoura.grid(row=6, column=2,  padx=10)									

		janela_pedra_papel_e_tesoura.mainloop()		

	func_pedra_papel_e_tesoura()

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
# | Configuração do Botão que aciona a funcionalidade Adivinha Número           |
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----	    

def botao_adivinha_numero():

	global numero_computador
	global count
	global historico_tentativas
	numero_computador = 0
	count = 0
	historico_tentativas = []

	def func_janela_regras():
		janela_regras = tk.Toplevel()
		janela_regras.title("Regras")
		janela_regras.geometry("1000x220")
		informacao_janela_regras = tk.Label(janela_regras, text="Essas são as regras do Adivinhador\n", font = ("Arial", 15, "bold"))
		informacao_janela_regras.pack()
		regra_1 = tk.Label(janela_regras, text="1° O valor de fim não pode ser menor que o valor de inicio\n", font = ("Arial", 10, "bold"))
		regra_1.pack()
		regra_2 = tk.Label(janela_regras, text="2° O valor de fim e inicio não podem ser iguais\n", font = ("Arial", 10, "bold"))
		regra_2.pack()
		regra_3 = tk.Label(janela_regras, text="3° É preciso que exista pelo menos 1 numero inteiro entre o inicio e fim\n", font = ("Arial", 10, "bold"))
		regra_3.pack()
		regra_4 = tk.Label(janela_regras, text="4° O valor fim não poderá exceder 34, para as posibilidades caberem na janela\n", font = ("Arial", 10, "bold"))
		regra_4.pack()
		regra_5 = tk.Label(janela_regras, text="5° O valor de inicio não pode ser menor que 1\n", font = ("Arial", 10, "bold"))
		regra_5.pack()


	def jogar():	
		global resultado
		global numero_inicio_int
		global numero_fim_int	
		global numero_computador
		global count
		global historico_tentativas
		global inserir_tentativa	
		global dica	
		try:
			tentativa_jogador_int = int(inserir_tentativa.get())	
			if tentativa_jogador_int > numero_computador and tentativa_jogador_int < numero_fim_int:
				count+=1
				historico_tentativas.append(inserir_tentativa.get())
				dica.config(text="O número que pensei é menor",  font = ("Arial", 10, "bold"))
			elif tentativa_jogador_int < numero_computador and tentativa_jogador_int > numero_inicio_int:
				count+=1
				historico_tentativas.append(inserir_tentativa.get())
				dica.config(text="O número que pensei é maior",  font = ("Arial", 10, "bold"))
			elif tentativa_jogador_int > numero_fim_int:
				count+=1
				historico_tentativas.append(inserir_tentativa.get())
				dica.config(text="Você precisa colocar um numero menor que o seu fim",  font = ("Arial", 10, "bold"))			
			elif tentativa_jogador_int < numero_inicio_int:
				count+=1
				historico_tentativas.append(inserir_tentativa.get())
				dica.config(text="Você precisa colocar um numero maior que o seu inicio",  font = ("Arial", 10, "bold"))
			elif tentativa_jogador_int == numero_computador:
				count+=1						
				historico_tentativas.append(inserir_tentativa.get())
				messagebox.showinfo("PARÁBENS", f"Você Acertou!\n Tentativas= {historico_tentativas}\n Total de Tentativas= {count}")
			elif tentativa_jogador_int == numero_inicio_int or tentativa_jogador_int == numero_fim_int:
				count+=1
				historico_tentativas.append(inserir_tentativa.get())
				dica.config(text="Coloque um valor inteiro dentro do limite estabelecido por você",  font = ("Arial", 10, "bold"))
			else:
				count+=1
				dica.config(text="Houve um erro",  font = ("Arial", 10, "bold"))

		except ValueError:
			dica.config(text= "O valor precisa ser um número inteiro e válido")						

	def possibilidades():
		global resultado
		global numero_inicio_int
		global numero_fim_int	
		global numero_computador
		global inserir_tentativa
		resultado.config(text=f"A maquina possui um número")
		posibilidades = list(range(numero_inicio_int + 1, numero_fim_int))
		possibilidades_jogador = tk.Label(janela_adivinha_numero, text=f"Posibilidades: {posibilidades}")
		possibilidades_jogador.pack()
		inserir_tentativa = tk.Entry(janela_adivinha_numero)
		inserir_tentativa.pack()
		botao_verificar = tk.Button(janela_adivinha_numero, text="Verificar", command=jogar)
		botao_verificar.pack()

	def gerar():
		global resultado
		global numero_inicio
		global numero_fim
		global numero_computador
		global botao_regras	
		global botao_regras_packado
		global possibilidades_jogador
		global numero_inicio_int
		global numero_fim_int
		try:
			numero_inicio_int = int(numero_inicio.get())
			numero_fim_int = int(numero_fim.get())
			numero_computador = randint(numero_inicio_int, numero_fim_int)
			if numero_inicio_int > numero_fim_int:
				resultado.config(text="Adicione uma entrada válida!\n Visite as regras")
			elif numero_fim_int == numero_inicio_int or numero_inicio_int == numero_fim_int:
				resultado.config(text="Adicione uma entrada válida!\n Visite as regras")
			elif (numero_fim_int-numero_inicio_int)==1:
				resultado.config(text="Adicione uma entrada válida!\n Visite as regras")
			elif numero_fim_int > 34:
				resultado.config(text="Adicione uma entrada válida!\n Visite as regras")
			elif numero_inicio_int <= 0:
				resultado.config(text="Adicione uma entrada válida!\n Visite as regras")
			else:
				while numero_computador == numero_fim_int or numero_computador == numero_inicio_int:
					numero_computador = randint(numero_inicio_int, numero_fim_int)
				possibilidades()

		except ValueError:
			resultado.config(text= "Adicione uma entrada válida!\n Visite as regras")

	def func_adivinha_numero():
		global resultado
		global janela_adivinha_numero	
		global numero_inicio
		global numero_fim
		global numero_inicio_int
		global numero_fim_int
		global dica
		janela_adivinha_numero = tk.Toplevel(menu)
		janela_adivinha_numero.title("Adivinha número")
		janela_adivinha_numero.geometry("800x400")
		informacao_janela_adivinha_numero= tk.Label(janela_adivinha_numero, text="Me informe um inicio e fim e escolherei um número entre esses números para você adivinhar", font = ("Arial", 13, "bold"))
		informacao_janela_adivinha_numero.pack()
		botao_regras = tk.Button(janela_adivinha_numero, text="Regras", command=func_janela_regras)
		# Configuração da Janela
		botao_gerar = tk.Button(janela_adivinha_numero, text="Gerar número", command=gerar)
		sinalizar_numero_inicio = tk.Label(janela_adivinha_numero, text="Inicio")
		numero_inicio = tk.Entry(janela_adivinha_numero)
		sinalizar_numero_inicio.pack()
		numero_inicio.pack()
		sinalizar_numero_fim = tk.Label(janela_adivinha_numero, text="Fim")
		numero_fim = tk.Entry(janela_adivinha_numero)
		sinalizar_numero_fim.pack()
		numero_fim.pack()
		botao_gerar.pack()
		botao_regras.pack()
		resultado = tk.Label(janela_adivinha_numero, text=f"A Máquina não possui um número")
		resultado.pack()
		dica = tk.Label(janela_adivinha_numero, text="Eu lhe direi se o número é maior ou menor do que pensei")
		dica.pack()

		janela_adivinha_numero.mainloop()

	func_adivinha_numero()				

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

