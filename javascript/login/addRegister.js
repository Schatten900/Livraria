document.addEventListener('DOMContentLoaded', () => {
    const loginURL = `http://${window.location.host}/login'`;
    
    function addRegister()
    {
        console.log('EAE');
        const username = document.getElementById('username');
        const email = document.getElementById('email');
        const password = document.getElementById('password');
        const confirm = document.getElementById('confirmPassword');

        fetch(`${loginURL}`,{
            method:'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: stringify({
                username: username,
                email: email,
                password: password,
                confirm: confirm,
                action: 'register'
            })
        })
            .then(response=>response.json())
            .then(data => {
                if (data.status == 'sucess') {
                console.log('Registrado com sucesso')
                window.location.href = '/index.html';
            }
            else {
                console.log('Houve um erro ao registrar:', data.message)
            }
        })
        .catch(error => console.error("Erro identificado",error));

        
    }
    if (document.getElementById('buttomRegister')) {
        document.getElementById('buttomRegister').addEventListener('click',addRegister());
    }
})