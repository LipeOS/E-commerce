const carouselContainer = document.querySelector('.carousel-container');
const slides = document.querySelectorAll('.carousel-slide');
const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next');

let currentIndex = 0;
const totalSlides = slides.length;

function updateCarousel() {
    const slideWidth = slides[0].clientWidth;
    carouselContainer.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
}

nextButton.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % totalSlides;
    updateCarousel();
});

prevButton.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
    updateCarousel();
});

// Ajustar o carrossel se a janela mudar de tamanho
window.addEventListener('resize', updateCarousel);


document.getElementById('cart-icon').addEventListener('click', function(event) {
    // Aqui você pode salvar o estado do carrinho no localStorage
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    
    // Adiciona lógica para salvar mais itens no carrinho, se necessário
    // Exemplo: cart.push('Produto novo');
    localStorage.setItem('cart', JSON.stringify(cart));
    
    // O redirecionamento já é tratado pelo link <a>
    // Se você quiser redirecionar via JS, poderia usar:
    // window.location.href = "nova-aba/index.html";
});
