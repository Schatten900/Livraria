document.addEventListener('DOMContentLoaded', () => {
    const buttom1 = document.getElementById("loginSwitch");
    const buttom2 = document.getElementById("registrarSwitch");
    const form = document.getElementById("Form");

    buttom1.addEventListener('click', () => {

        document.getElementById("textoForm").innerHTML = "Login Form";
        switchUserForm(buttom1, buttom2);
        removeRegisterFields(form);
        addLoginFields(form);
    });

    buttom2.addEventListener('click', () => {
        document.getElementById("textoForm").innerHTML = "Registro Form";
        switchUserForm(buttom2, buttom1);

        removeLoginFields(form);
        addRegisterFields(form);
    });


    function switchUserForm(buttomON, buttomOFF) {
        buttomON.classList.add('activeButtom');
        buttomOFF.classList.remove('activeButtom');
    }

    function addLoginFields(form) {
        if (!document.getElementById('username')) {
            const userField = document.createElement('div');
            userField.classList.add("formField");
            userField.innerHTML = "<input type='text' id='username' placeholder='Username'>";

            form.appendChild(userField);
            const username = document.getElementById('username');
            username.classList.add("inputField");
        }

        if (!document.getElementById('password')) {
            const passwordField = document.createElement('div');
            passwordField.classList.add("formField");
            passwordField.innerHTML = "<input type='password' id='password' placeholder='Password'>";
            form.appendChild(passwordField);
            const password = document.getElementById('password');
            password.classList.add("inputField");
        }

        if (!document.getElementById('buttomEnter')) {
            const buttomEnter = document.createElement('button');
            buttomEnter.id = 'buttomEnter';
            buttomEnter.textContent = "Login";
            buttomEnter.classList.add("buttomLogin");
            form.appendChild(buttomEnter);
        }
    }

    function addRegisterFields(form) {
        if (!document.getElementById('username')) {
            const userField = document.createElement('div');
            userField.classList.add("formField");
            userField.innerHTML = "<input type='text' id ='username' placeholder = 'Username'>";

            form.appendChild(userField);
            const username = document.getElementById('username');
            username.classList.add("inputField");
        }

        if (!document.getElementById('email')) {
            const emailField = document.createElement('div');
            emailField.classList.add("formField");
            emailField.innerHTML = "<input type='email' id ='email' placeholder = 'Email'>";

            form.appendChild(emailField);
            const email = document.getElementById('email');
            email.classList.add("inputField");
        }

        if (!document.getElementById('password')) {
            const passwordField = document.createElement('div');
            passwordField.classList.add("formField");
            passwordField.innerHTML = "<input type='password' id ='password' placeholder = 'Password'>";

            form.appendChild(passwordField);
            const password = document.getElementById('password');
            password.classList.add("inputField");
        }

        if (!document.getElementById('confirmPassword')) {
            const confirmField = document.createElement('div');
            confirmField.classList.add("formField");
            confirmField.innerHTML = "<input type='password' id ='confirmPassword' placeholder = 'ConfirmPassword'>";

            form.appendChild(confirmField);
            const confirm = document.getElementById('confirmPassword');
            confirm.classList.add("inputField");
        }

        if (!document.getElementById('buttomEnter')) {
            const buttomEnter = document.createElement('button');
            buttomEnter.id = "buttomEnter";
            buttomEnter.textContent = "Registrar";
            buttomEnter.classList.add("buttomLogin");
            form.appendChild(buttomEnter);
        }
    }


    function removeLoginFields(form) {
        const userField = document.getElementById('username');
        const passwordField = document.getElementById('password');
        const buttomEnter = document.getElementById('buttomEnter');

        if (userField) {
            form.removeChild(userField.parentElement);
        }
        if (passwordField) {
            form.removeChild(passwordField.parentElement);
        }
        if (buttomEnter) {
            form.removeChild(buttomEnter);
        }
    }

    function removeRegisterFields(form) {
        const userField = document.getElementById('username');
        const passwordField = document.getElementById('password');
        const buttomEnter = document.getElementById('buttomEnter');
        const confirmField = document.getElementById('confirmPassword');
        const emailField = document.getElementById('email')

        if (userField) {
            form.removeChild(userField.parentElement);
        }
        if (passwordField) {
            form.removeChild(passwordField.parentElement);
        }
        if (buttomEnter) {
            form.removeChild(buttomEnter);
        }
        if (confirmField) {
            form.removeChild(confirmField.parentElement);
        }
        if (emailField) {
            form.removeChild(emailField.parentElement);
        }
    }
});
