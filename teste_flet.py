import flet as ft

def main(page):
    # Título da página
    page.title = "Contador de Letras"
    
    # Criando os widgets de entrada e botão
    texto_input = ft.TextField(label="Digite um Texto", autofocus=True)
    resultado_texto = ft.Text()

    # Função para contar as letras quando o botão for pressionado
    def contar_letras(e):
        # Obtendo o texto digitado
        texto = texto_input.value.lower()  # Normaliza para minúsculas
        contagem = {}

        # Contando as letras
        for letra in texto:
            if letra.isalpha():  # Só conta se for uma letra
                if letra in contagem:
                    contagem[letra] += 1
                else:
                    contagem[letra] = 1
        
        # Exibindo o resultado no Text
        resultado_texto.value = str(contagem)
        page.update()

    # Criando um botão para contar as letras
    contar_button = ft.ElevatedButton("Contar Letras", on_click=contar_letras)

    # Adicionando os widgets à página
    page.add(texto_input, contar_button, resultado_texto)

# Inicializando o aplicativo Flet
ft.app(target=main)