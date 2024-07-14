document.addEventListener('DOMContentLoaded', () => {
    const loginURL = `http://${window.location.host}/login`;

    window.addRegister = function (event) {
        event.preventDefault();
        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirm = document.getElementById('confirmPassword').value;


        if (username.length == 0 || email.length == 0 || password.length == 0 || confirm.length == 0) {
            window.alert("Um ou mais dos campos não foram preenchidos")
        }

        fetch(loginURL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                email: email,
                password: password,
                confirm: confirm,
                action: 'register'
            })
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                if (data.status === 'sucess') {
                    console.log("Registrado com sucesso");
                    window.location.href = data.redirect;
                }
                else {
                    window.alert("Algum ou mais dados podem estar incorretos.");
                    console.log('Houve um erro ao registrar:', data.message);
                }
            })
            .catch(error => console.error("Erro identificado", error));


    }
    if (document.getElementById('buttomRegister')) {
        document.getElementById('buttomRegister').addEventListener('click', addRegister);
    }
});