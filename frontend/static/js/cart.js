document.addEventListener("DOMContentLoaded", function() {
    const selectItems = document.querySelectorAll('.select-item');
    const totalPriceElement = document.getElementById('total-price');

    // Função para calcular o total com base nos itens selecionados
    function calculateTotal() {
        let total = 0.0;

        selectItems.forEach(item => {
            if (item.checked) {
                const itemId = item.getAttribute('data-item-id');
                const priceElement = document.querySelector(`.cart-item[data-item-id="${itemId}"] .item-price p`);
                const price = parseFloat(priceElement.innerText.replace('R$', '').trim());
                total += price;
            }
        });

        totalPriceElement.innerText = total.toFixed(2);
    }

    // Adicionar evento de click em cada checkbox para recalcular o total
    selectItems.forEach(item => {
        item.addEventListener('change', calculateTotal);
    });

    // Função para finalizar a compra com os itens selecionados
    const checkoutBtn = document.querySelector('.checkout-btn');
    checkoutBtn.addEventListener('click', function() {
        const selectedItems = Array.from(selectItems)
            .filter(item => item.checked)
            .map(item => item.getAttribute('data-item-id'));

        if (selectedItems.length > 0) {
            // Envia os itens selecionados para o servidor (implementação do back-end necessária)
            alert(`Itens selecionados para compra: ${selectedItems.join(', ')}`);
        } else {
            alert("Nenhum item selecionado.");
        }
    });
});
