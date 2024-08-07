from servicos.connection import executeQuery,Error
from dominios.Livros import Book


class Estoque():
    def __init__(self):
        self.id = 0

    def get(self):
        return self.id
    
    def set(self,idAux):
        self.id = idAux

    def criar(self):
        try:
            QUERY = "INSERT INTO Estoque (IdEstoque,AvaliacaoEstoque) VALUES(%s,%s)"
            params = (self.id,0,)
            executeQuery(QUERY,params)
            return True
    
        except ValueError as e:
            print(f"Erro na adicao:{e}")
            return False

    def adicionar(self,titulo,autor,quantidade,preco):
        livro = Book()
        livro.setLivro(titulo,autor)
        try:
            QUERY = "SELECT * FROM Livro WHERE ISBN = %s"
            result = executeQuery(QUERY,livro.getISBN())
            if len(result) == 0:
                QUERY2 = "INSERT INTO Livro (ISBN,Titulo,Autor,Descricao) VALUES (%s,%s,%s,%s)"
                params = (livro.getISBN(),
                        livro.getTitle(),
                        livro.getAuthor(),
                        livro.getDescription(),
                        )
                executeQuery(QUERY2,params) 
            
            QUERY3 = "INSERT INTO LivroEstoque (IdEstoque,ISBN,Preco,Quantidade) VALUES (%s,%s,%s,%s)"
            params = (self.id,livro.getISBN(),preco,quantidade)
            executeQuery(QUERY3,params)
            return True

        except ValueError as e:
            print(f"Erro na adicao:{e}")
            return False
    
    def remover(self,titulo,autor):
        try:
            livro = Book()
            livro.setLivro(titulo,autor)
            isbn = livro.getISBN()
            print(titulo)
            print(autor)
            print(isbn)
            print(self.id)
            QUERY = "DELETE FROM LivroEstoque WHERE ISBN = %s and IdEstoque = %s"
            params = (isbn,self.id,)
            executeQuery(QUERY,params)
            return True
    
        except ValueError as e:
            print(e)
            return False

    def editar(self):
        try:
            pass
        except ValueError as e:
            print(e)

    def select(self):
        try:
            QUERY = """
            SELECT L.Titulo,L.Autor, E.Preco, E.Quantidade
            FROM LivroEstoque as E
            INNER JOIN Livro as L ON E.ISBN = L.ISBN
            WHERE E.IdEstoque = %s
            """ 
        
            books = executeQuery(QUERY,self.id)
            return books
        
        except ValueError as e:
            print(e)
            return None