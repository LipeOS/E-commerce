document.addEventListener("DOMContentLoaded", function() {
    const buyButtons = document.querySelectorAll('.btn-buy');

    buyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const produtoId = this.getAttribute('data-produto-id');
            addToCart(produtoId);
        });
    });

    function addToCart(produtoId) {
        fetch(`/adicionar_ao_carrinho/${produtoId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: produtoId })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('Produto adicionado ao carrinho!');
            } else {
                alert('Erro ao adicionar produto: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Erro:', error);
        });
    }
});
