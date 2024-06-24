document.addEventListener('DOMContentLoaded', () => {

    const loginURL = `http://${window.location.host}/login'`;
    function loginCheck() {

        const loginEmail = document.getElementById('email').value;
        const loginPassword = document.getElementById('password').value

        fetch(`${loginURL}/login`, {
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
                if (data.status == 'sucess') {
                    console.log('Logado com sucesso')
                    window.location.href = '/index.html';
                }
                else {
                    console.log("Houve um erro ao logar:", data.message)
                }
            })
            .catch(error => console.error("Error ao buscar dados: ", error));

    }
    if (document.getElementById('buttomLogin')) {
        document.getElementById('buttomLogin').addEventListener('click', loginCheck());
    }
})