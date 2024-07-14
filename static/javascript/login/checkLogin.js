document.addEventListener('DOMContentLoaded', () => {

    const loginURL = `http://${window.location.host}/login`;

    window.loginCheck = function (event) {
        event.preventDefault();
        const loginEmail = document.getElementById('email').value;
        const loginPassword = document.getElementById('password').value

        if (loginEmail.length == 0 || loginPassword.length == 0) {
            window.alert("Um ou mais dos campos não foram preenchidos")
        }

        fetch(loginURL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: loginEmail,
                password: loginPassword,
                action: 'login'
            })
        })
            .then(response => response.json())
            .then(data => {
                if (data.status === "sucess") {
                    console.log("Logado com sucesso");
                    window.location.href = data.redirect;
                }
                else {
                    window.alert("Algum ou mais dados podem estar incorretos");
                    console.log("Houve um erro ao logar:", data.message);
                }
            })
            .catch(error => console.error("Error ao buscar dados: ", error));

    }
    if (document.getElementById('buttomLogin')) {
        document.getElementById('buttomLogin').addEventListener('click', loginCheck);
    }
})