document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('addProductForm');

    document.getElementById('addProduct').addEventListener('click',function()
    {
        showFormAdd(form);
    });

    document.getElementById('addProductButtom').addEventListener('click',function()
    {
        showFormAdd(form);
    });


});

function showFormAdd(form)
{
    if (form.style.display == "block")
        {
            form.style.display = "none";
        }
        else
        {
            form.style.display = "block";
        }
}

