import tkinter as tk

# Definindo as funções de cálculo e classificação do IMC

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificacao_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso\nProcure um nutricionista que possa lhe informar sobre ganho de massa e melhores formas de atingir seu peso ideal"
    elif 18.5 <= imc < 24.9:
        return "Peso normal\nParabéns! manter uma vida saudável é essencial para termos uma longa vida !"
    elif 25.0 <= imc < 30.0:
        return "Sobrepeso\nTome cuidado com sua alimentação para não adquirir problemas futuros, busque se exercitar mais. VOCÊ CONSEGUE."
    elif 30.0 <= imc < 34.9:
        return "Obesidade Grau I\nBusque ajuda médica, não deixe que seu grau de IMC piore sua qualidade de vida."
    elif 35.0 <= imc < 39.9:
        return "Obesidade Grau II\nBusque ajuda médica o mais rápido possível, não deixe que seu grau de IMC piore sua qualidade de vida."
    else:
        return "Obesidade Grau III\nBusque ajuda médica URGENTEMENTE, não deixe que seu grau de IMC piore sua qualidade de vida."
    
def substituir_virgula_por_ponto(texto):
    return texto.replace(',', '.')

# Função para calcular e exibir o IMC
def calcular():
    nome = entrada_nome.get()
    idade = int(entrada_idade.get())
    peso = float(substituir_virgula_por_ponto(entrada_peso.get()))
    altura = float(substituir_virgula_por_ponto(entrada_altura.get()))
    imc = calcular_imc(peso, altura)
    classificacao = classificacao_imc(imc)
    
    # Exibindo os resultados
    resultado.config(text=f'{nome}\nIdade: {idade} anos\nIMC: {imc:.2f}\n')
    
    # Ajusta a cor do texto
    if "Obesidade Grau III" in classificacao:
        classificacao_imc_label.config(text=f"Classificação do IMC: {classificacao}", fg='red')
    elif "Obesidade Grau II" in classificacao:
        classificacao_imc_label.config(text=f"Classificação do IMC: {classificacao}", fg='red')
    elif "Obesidade Grau I" in classificacao:
        classificacao_imc_label.config(text=f"Classificação do IMC: {classificacao}", fg='red')
    elif "Sobrepeso" in classificacao:
        classificacao_imc_label.config(text=f"Classificação do IMC: {classificacao}", fg='orange')
    elif "Abaixo do peso" in classificacao:
        classificacao_imc_label.config(text=f"Classificação do IMC: {classificacao}", fg='orange')
    else:
        classificacao_imc_label.config(text=f"Classificação do IMC: {classificacao}", fg='black')

# Criação da janela principal
janela = tk.Tk()
janela.title('Calculadora IMC')
janela.geometry("1700x1800")
janela.configure(bg="#f0f0f0")

# Criação de um frame centralizado
frame_central = tk.Frame(janela, bg="#f0f0f0")
frame_central.place(relx=0.5, rely=0.5, anchor='center')

# Configurando o estilo dos widgets
estilo_label = {'bg': '#f0f0f0', 'font': ('Arial', 12)}
estilo_entry = {'font': ('Arial', 12)}
estilo_button = {'font': ('Arial', 12, 'bold'), 'bg': '#007acc', 'fg': 'white'}

# Centralizar os widgets no frame
frame_central.grid_columnconfigure(0, weight=1)
frame_central.grid_columnconfigure(1, weight=1)

# Widgets de entrada de dados
tk.Label(frame_central, text='Nome do usuário:       ', **estilo_label).grid(row=0, column=0, padx=10, pady=10, sticky='e')
entrada_nome = tk.Entry(frame_central, **estilo_entry)
entrada_nome.grid(row=0, column=1, padx=10, pady=10, sticky='w')

tk.Label(frame_central, text='Idade do Usuário:       ', **estilo_label).grid(row=1, column=0, padx=10, pady=10, sticky='e')
entrada_idade = tk.Entry(frame_central, **estilo_entry)
entrada_idade.grid(row=1, column=1, padx=10, pady=10, sticky='w')

tk.Label(frame_central, text='Peso do Usuário (kg):', **estilo_label).grid(row=2, column=0, padx=10, pady=10, sticky='e')
entrada_peso = tk.Entry(frame_central, **estilo_entry)
entrada_peso.grid(row=2, column=1, padx=10, pady=10, sticky='w')

tk.Label(frame_central, text='Altura do Usuário (m):', **estilo_label).grid(row=3, column=0, padx=10, pady=10, sticky='e')
entrada_altura = tk.Entry(frame_central, **estilo_entry)
entrada_altura.grid(row=3, column=1, padx=10, pady=10, sticky='w')

# Botão para calcular o IMC
botao_calcular = tk.Button(frame_central, text="Calcular IMC", command=calcular, **estilo_button)
botao_calcular.grid(row=4, columnspan=2, padx=10, pady=20)

# Labels para exibir os resultados
resultado = tk.Label(frame_central, text="", **estilo_label)
resultado.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

classificacao_imc_label = tk.Label(frame_central, text="", **estilo_label)
classificacao_imc_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Iniciando o loop principal da interface gráfica
janela.mainloop()

