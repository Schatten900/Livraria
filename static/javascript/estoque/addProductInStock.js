document.addEventListener('DOMContentLoaded', () => {
    const addBookURL = `http://${window.location.host}/estoque`;
    window.AddBookInStock = function (event) {
        event.preventDefault();

        const titleBook = document.getElementById("inputTitle").value;
        const authorBook = document.getElementById("inputAuthor").value;
        const qntdBook = document.getElementById("inputQntd").value;
        const priceBook = document.getElementById("inputPrice").value;

        if (qntdBook > 30)
            window.alert("Maximo de 30 livros para cadastrar.");

        if (!qntdBook || !priceBook || !authorBook || !titleBook)
            window.alert("Preencha todos os dados corretamente.");

        let generos = [];
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach(checkbox =>{
            if (checkbox.checked){
                //pegar a label que acompanha a checkbox
                genero = checkbox.value
                generos.push(genero);
                console.log(genero)
            }
        })

        contentBook = {
            action: 'add',
            title: titleBook,
            author: authorBook,
            quantity: qntdBook,
            price: priceBook,
            generos:generos
        }

        fetch(addBookURL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(contentBook)
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('HTTP ERROR: ', response.status);
                }
                return response.json;
            })
            .then(data => {
                if (data === 'success') {
                    console.log("Adicionado com sucesso");
                }
                else {
                    window.alert("Verifique os dados corretamente.");
                    console.log("Erro na adicao do livro");
                }
            })
            .catch(error => console.error("Erro identificado", error));
    }
    if (document.getElementById('addProductButtom')) {
        document.getElementById('addProductButtom').addEventListener('click', AddBookInStock);
    }
})