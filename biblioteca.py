import os
from livro import Livros

class Biblioteca:
    def __init__(self, livros=None):
        if livros is None:
            self.livros = []
        else:
            self.livros = livros

    def guardar_livros(self):
        with open('biblioteca.txt', 'w') as ficheiro:
            for livro in self.livros:
                ficheiro.write(f"{livro.titulo},{livro.autor},{livro.preco},{livro.genero},{livro.quantidade_de_paginas}\n")

    def carregar_livros(self):
        try:
            with open('biblioteca.txt', 'r') as ficheiro:
                self.livros = []  # Limpa a lista antes de carregar
                for linha in ficheiro:
                    titulo, autor, preco, genero, quantidade_de_paginas = linha.strip().split(',')
                    self.livros.append(Livros(titulo, autor, float(preco), genero, int(quantidade_de_paginas)))
        except FileNotFoundError:
            print("Arquivo 'biblioteca.txt' não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar livros: {e}")

    def mostrar_livros(self):
        if not self.livros:
            return "Não há livros na biblioteca."
        resultado = ""
        for livro in self.livros:
            resultado += f"Título: {livro.titulo}, Autor: {livro.autor}, Preço: {livro.preco}, Gênero: {livro.genero}, Quantidade de páginas: {livro.quantidade_de_paginas}\n"
        return resultado

    def registar_livro(self, titulo, autor, preco, genero, quantidade_de_paginas):
        self.livros.append(Livros(titulo, autor, preco, genero, quantidade_de_paginas))
        self.guardar_livros()
        return "Livro registado com sucesso."

    def editar_livro(self, titulo_editar, novo_titulo, novo_autor, novo_preco, novo_genero, nova_quantidade_de_paginas):
        if not titulo_editar:
            return "Por favor, insira o título do livro a editar."

        for livro in self.livros:
            if livro.titulo == titulo_editar:
                livro.titulo = novo_titulo
                livro.autor = novo_autor
                livro.preco = novo_preco
                livro.genero = novo_genero
                livro.quantidade_de_paginas = nova_quantidade_de_paginas
                self.guardar_livros()
                return "Livro editado com sucesso!"
        return "Livro não encontrado."

    def remover_livro(self, titulo_remover):
        livro_encontrado = False
        for livro in self.livros:
            if livro.titulo == titulo_remover:
                self.livros.remove(livro)
                livro_encontrado = True
                break
        if livro_encontrado:
            self.guardar_livros()
            return "Livro removido com sucesso!"
        else:
            return "Livro não encontrado."

    def procurar_livro_por_titulo(self, titulo_procurar):
        for livro in self.livros:
            if livro.titulo == titulo_procurar:
                return f"Título: {livro.titulo}, Autor: {livro.autor}, Preço: {livro.preco}, Gênero: {livro.genero}, Quantidade de páginas: {livro.quantidade_de_paginas}"
        return "Livro não encontrado."
