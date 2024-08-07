document.addEventListener('DOMContentLoaded', () => {
    const removeBookURL = `http://${window.location.host}/estoque`;
    window.RemoveBookInStock = function (event) {
        event.preventDefault();
        let cont = 0;
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                //remove a div da tela
                const ProductRemoved = checkbox.closest('.productItem');
                const parentElement = ProductRemoved.parentNode;

                const titleElem = ProductRemoved.querySelector("#titleProduct");
                const authorElem = ProductRemoved.querySelector("#authorProduct");

                const titulo = titleElem.innerText;
                const autor = authorElem.innerText;

                parentElement.removeChild(ProductRemoved);

                console.log(titulo);
                console.log(autor);

                //remover do banco de dados
                requisicao = {
                    "title": titulo,
                    "author": autor,
                    "action": "remove"
                }

                fetch(removeBookURL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(requisicao)
                })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('HTTP ERROR: ', response.status);
                        }
                        return response.json;
                    })
                    .then(data => {
                        if (data.status === "sucess") {
                            console.log("Removido com sucesso");
                        }
                        else {
                            window.alert("Verifique os marcados corretamente.");
                            console.log("Erro na remoção do livro");
                        }
                    })
                    .catch(error => console.error("Erro identificado", error));
                cont++;
            }
        });
        if (cont == 0) {
            alert("Selecione ao menos um produto");
        }
    }
    if (document.getElementById('removeProductButtom')) {
        document.getElementById('removeProductButtom').addEventListener('click', RemoveBookInStock);
    }
})