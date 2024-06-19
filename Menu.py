import tkinter as tk
from tkinter import messagebox
from biblioteca import Biblioteca

class BibliotecaApp:
    def __init__(self, root):
        self.biblioteca = Biblioteca()
        self.biblioteca.carregar_livros()
        self.root = root

        self.frame = tk.Frame(root, bg="white")
        titulo_label = tk.Label(self.frame, text="Biblioteca", font=("Arial", 24), fg="black", width= 20, bg="white")
        titulo_label.pack(pady=20)
        self.frame.pack(padx=10, pady=10)

        self.btn_registrar = tk.Button(self.frame, text="Registrar Livro", command=self.registrar_livro, font=("Arial", 16), height=2, width=20, bg="white", fg="black")
        self.btn_registrar.pack(fill=tk.X,pady=10)

        self.btn_mostrar = tk.Button(self.frame, text="Mostrar Livros", command=self.mostrar_livros, font=("Arial", 16), height=2, width=20, bg="white", fg="black")
        self.btn_mostrar.pack(fill=tk.X, pady=10)

        self.btn_editar = tk.Button(self.frame, text="Editar Livro", command=self.editar_livro, font=("Arial", 16), height=2, width=20, bg="white", fg="black")
        self.btn_editar.pack(fill=tk.X, pady=10)

        self.btn_remover = tk.Button(self.frame, text="Remover Livro", command=self.remover_livro, font=("Arial", 16), height=2, width=20, bg="white", fg="black")
        self.btn_remover.pack(fill=tk.X, pady=10)

        self.btn_procurar = tk.Button(self.frame, text="Procurar Livro", command=self.procurar_livro, font=("Arial", 16), height=2, width=20, bg="white", fg="black")
        self.btn_procurar.pack(fill=tk.X, pady=10)

        self.btn_sair = tk.Button(self.frame, text="Sair", command=root.quit, font=("Arial", 16), height=2, width=20, bg="white", fg="black")
        self.btn_sair.pack(fill=tk.X, pady=10)

    def registrar_livro(self):
        self.formulario_livro("Registrar Livro", self.biblioteca.registar_livro)

    def mostrar_livros(self):
        resultado = self.biblioteca.mostrar_livros()
        messagebox.showinfo("Livros na Biblioteca", resultado)

    def editar_livro(self):
        self.formulario_editar("Editar Livro", self.biblioteca.editar_livro)

    def remover_livro(self):
        titulo = self.input_dialog("Remover Livro", "Título:")
        if titulo:
            resultado = self.biblioteca.remover_livro(titulo)
            messagebox.showinfo("Remover Livro", resultado)

    def procurar_livro(self):
        titulo = self.input_dialog("Procurar Livro", "Título:")
        if titulo:
            resultado = self.biblioteca.procurar_livro_por_titulo(titulo)
            messagebox.showinfo("Procurar Livro", resultado)

    def formulario_livro(self, title, callback):
        form = tk.Toplevel(self.root)
        form.title(title)

        labels = ["Título", "Autor", "Preço", "Gênero", "Quantidade de Páginas"]
        entries = []

        for label in labels:
            frame = tk.Frame(form, bg="white")
            frame.pack(pady=5)
            lbl = tk.Label(frame, text=label, bg="white", fg="black")
            lbl.pack(side=tk.LEFT)
            entry = tk.Entry(frame, width=30, font=("Arial", 16), bg="white", fg="black")
            entry.pack(side=tk.RIGHT)
            entries.append(entry)

        def submit():
            titulo = entries[0].get()
            autor = entries[1].get()
            try:
                preco = float(entries[2].get())
            except ValueError:
                messagebox.showerror("Erro", "Preço deve ser um número.")
                return
            genero = entries[3].get()
            try:
                quantidade_de_paginas = int(entries[4].get())
            except ValueError:
                messagebox.showerror("Erro", "Quantidade de páginas deve ser um número.")
                return

            if autor.isdigit():
                messagebox.showerror("Erro", "Autor não pode conter números.")
                return
            if genero.isdigit():
                messagebox.showerror("Erro", "Gênero não pode conter números.")
                return

            resultado = callback(titulo, autor, preco, genero, quantidade_de_paginas)
            messagebox.showinfo(title, resultado)
            form.destroy()

        btn_submit = tk.Button(form, text="Enviar", command=submit, width=30, bg="white", fg="black")
        btn_submit.pack(pady=10)

    def formulario_editar(self, title, callback):
        form = tk.Toplevel(self.root)
        form.title(title)
        form.geometry("500x300")

        lbl_titulo = tk.Label(form, text="Título do Livro a Editar:", bg="white", fg="black")
        lbl_titulo.pack()
        entry_titulo = tk.Entry(form, width=30, font=("Arial", 16), bg="white", fg="black")
        entry_titulo.pack()

        labels = ["Novo Título", "Novo Autor", "Novo Preço", "Novo Gênero", "Nova Quantidade de Páginas"]
        entries = []

        for label in labels:
            frame = tk.Frame(form, bg="white")
            frame.pack(pady=5)
            lbl = tk.Label(frame, text=label, bg="white", fg="black")
            lbl.pack(side=tk.LEFT)
            entry = tk.Entry(frame, width=30, font=("Arial", 16), bg="white", fg="black")
            entry.pack(side=tk.RIGHT)
            entries.append(entry)

        def submit():
            titulo_editar = entry_titulo.get()
            novo_titulo = entries[0].get()
            novo_autor = entries[1].get()
            try:
                novo_preco = float(entries[2].get())
            except ValueError:
                messagebox.showerror("Erro", "Preço deve ser um número.")
                return
            novo_genero = entries[3].get()
            try:
                nova_quantidade_de_paginas = int(entries[4].get())
            except ValueError:
                messagebox.showerror("Erro", "Quantidade de páginas deve ser um número.")
                return

            if novo_autor.isdigit():
                messagebox.showerror("Erro", "Autor não pode conter números.")
                return
            if novo_genero.isdigit():
                messagebox.showerror("Erro", "Gênero não pode conter números.")
                return

            resultado = callback(titulo_editar, novo_titulo, novo_autor, novo_preco, novo_genero, nova_quantidade_de_paginas)
            messagebox.showinfo(title, resultado)
            form.destroy()

        btn_submit = tk.Button(form, text="Enviar", command=submit, width=30, bg="white", fg="black")
        btn_submit.pack(pady=10)

    def input_dialog(self, title, prompt):
        form = tk.Toplevel(self.root)
        form.title(title)
        form.geometry("300x100")

        lbl = tk.Label(form, text=prompt, bg="white", fg="black")
        lbl.pack()
        entry = tk.Entry(form, width=30, font=("Arial", 16), bg="white", fg="black")
        entry.pack()

        def submit():
            form.result = entry.get()
            form.destroy()

        btn_submit = tk.Button(form, text="Enviar", command=submit, width=30, bg="white", fg="black")
        btn_submit.pack(pady=10)

        form.transient(self.root)
        form.grab_set()
        self.root.wait_window(form)
        return getattr(form, 'result', None)

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.geometry("800x600") 
    root.configure(bg="white")
    root.mainloop()
