#Projeto para buscar nomes de musicas utilizando a API do Deezer(API significa Application Programming Interface (Interface de Programação de Aplicação).)

#Primeiro vamos importar as bibliotecas customtkinter e requests
import customtkinter as ctk 
import requests

#configurando o tema da interface
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

# criando a função 
def buscar_musica():
    # Aqui se obtem o nome da música na caixa de texto
    nome_musica = entry.get()

    if nome_musica:
        # Aqui eu coloquei a API do Deezer para buscar músicas
        url = f"https://api.deezer.com/search?q={nome_musica}"

        # Fazendo a requisição à API
        response = requests.get(url)

        # verificando se a requisição foi bem sucedida
        if response.status_code == 200:
            dados = response.json()

            resultado_text.delete(1.0, ctk.END)

            if dados.get('data'):
                resultado_text.insert(ctk.END, f"Resultado para '{nome_musica}':\n\n")
                for musica in dados['data']:
                    resultado_text.insert(ctk.END, f"Título: {musica['title']}\n")
                    resultado_text.insert(ctk.END, f"Artista: {musica['artist']['name']}\n")
                    resultado_text.insert(ctk.END, f"Álbum: {musica['album']['title']}\n")
                    resultado_text.insert(ctk.END, f"Duração: {musica['duration']} segundos\n")
                    resultado_text.insert(ctk.END, f"Link: {musica['link']}\n")
                    resultado_text.insert(ctk.END, "_"*40 + "\n")
            else:
                resultado_text.insert(ctk.END, f"Nenhum resultado encontrado para '{nome_musica}'.")
        else:
            resultado_text.insert(ctk.END, f"Erro na requisição: '{response.status_code}'")
    else:
        resultado_text.insert(ctk.END, "Por favor, insira o nome de uma música.")

# janela principal
janela = ctk.CTk()
janela.title('Meu Buscador de Músicas Personalizado @By Franco versão 1.0/2025')
janela.geometry('600x400')

frame = ctk.CTkFrame(janela)
frame.pack(pady=20, padx=20, fill='both', expand=True)

entry = ctk.CTkEntry(frame, placeholder_text='Digite o nome da música...', width=400)
entry.pack(pady=10)

botao_buscar = ctk.CTkButton(frame, text='Buscar Música', command=buscar_musica)
botao_buscar.pack(pady=10)

resultado_text = ctk.CTkTextbox(frame, width=500, height=200)
resultado_text.pack(pady=10)

janela.mainloop()







