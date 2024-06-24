document.getElementById("removeProduct").addEventListener('click',function()
{
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    removeDiv(checkboxes);
        
});

function removeDiv(checkboxes)
{
    let cont = 0;
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