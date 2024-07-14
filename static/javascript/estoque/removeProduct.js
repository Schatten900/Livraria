function RemoveBookInStock(){

    let cont = 0;
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        if (checkbox.checked)
        {
            const divToRemove = checkbox.closest('.productItem');
            const parentElement = divToRemove.parentNode;
            parentElement.removeChild(divToRemove);
            cont++;
        }
    });
    if (cont == 0)
    {
        alert("Selecione ao menos um produto");
    }

}