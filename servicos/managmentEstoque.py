from servicos.connection import executeQuery,Error
from dominios.Livros import Book

def addBookEstoque(ID,titulo,autor,descricao,quantidade,preco):
    livro = Book()
    ISBN = livro.getISBN(titulo,autor)
    livro.setISBN(ISBN)
    livro.setDescription(descricao)
    bookInfo = {
        'ISBN':ISBN,
        'Titulo':titulo,
        'Autor':autor,
        'Preco':preco,
        'Descricao':descricao
    }
    try:
        QUERY = "SELECT * FROM Livro WHERE ISBN = %s"
        result = executeQuery(QUERY,bookInfo['ISBN'])
        if len(result) == 0:
            QUERY2 = "INSERT INTO Livro (ISBN,Titulo,Autor,Preco,Descricao) VALUES (%s,%s,%s,%s,%s)"
            params = (bookInfo['ISBN'],
                      bookInfo['Titulo'],
                      bookInfo['Autor'],
                      bookInfo['Preco'],
                      bookInfo['Descricao']
                      )
            executeQuery(QUERY2,params) 
        
        QUERY3 = "INSERT INTO estoque_livro (ID_Estoque,ISBN_Livro,Quantidade,preco,avaliacao) VALUES (%s,%s,%s,%s,%s)"
        params = (ID,bookInfo['ISBN'],quantidade,preco,0)
        executeQuery(QUERY3,params)
        print("Adicionado com sucesso")
    except ValueError as e:
        print(e)

def removeBookEstoque(ISBN,ID):
    try:
        QUERY = "DELETE FROM estoque_livro WHERE ISBN_Livro = %s and ID_Estoque = %s"
        params = (ISBN,ID)
        executeQuery(QUERY,params)
        print("Removido com sucesso")
    except ValueError as e:
        print(e)

def editBookEstoque(ISBN,ID,quantidade=None,preco=None):
    try:
        if quantidade and preco:
            QUERY = """UPDATE estoque_livro SET quantidade = %s, preco = %s WHERE ID_Estoque = %s and ISBN_Livro = %s """
            params = (
                quantidade,
                preco,
                ID,
                ISBN
            )
            executeQuery(QUERY,params)
        if quantidade and not preco:
            QUERY = """UPDATE estoque_livro SET quantidade = %s WHERE ID_Estoque = %s and ISBN_LIVRO = %s"""
            params = (
                quantidade,
                ID,
                ISBN
            )
            executeQuery(QUERY,params)
        if not quantidade and preco:
            QUERY = """UPDATE estoque_livro SET preco = %s WHERE ID_Estoque = %s and ISBN_LIVRO = %s"""
            params = (
                preco,
                ID,
                ISBN
            )
            executeQuery(QUERY,params)

        print("Modificado com sucesso")
    except ValueError as e:
        print(e)

def selectBooks(ID_USER):
    try:
        QUERY = """
        SELECT L.titulo, E.preco, E.quantidade
        FROM Estoque_livro as E
        INNER JOIN Livro as L ON E.ISBN_Livro = L.ISBN
        WHERE E.ID_Estoque = %s
        """ 
    
        books = executeQuery(QUERY,ID_USER)
        return books
    
    except ValueError as e:
        print(e)