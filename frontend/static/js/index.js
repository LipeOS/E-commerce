const carouselContainer = document.querySelector('.carousel-container');
const slides = document.querySelectorAll('.carousel-slide');

let currentIndex = 0;
const totalSlides = slides.length;

function updateCarousel() {
    const slideWidth = slides[0].clientWidth;
    carouselContainer.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
}

// Auto avançar o carrossel a cada 4 segundos
setInterval(() => {
    currentIndex = (currentIndex + 1) % totalSlides;
    updateCarousel();
}, 4000);

// Ajustar o carrossel se a janela mudar de tamanho
window.addEventListener('resize', updateCarousel);

document.getElementById('cart-icon').addEventListener('click', function(event) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    // Adicione lógica para salvar mais itens no carrinho, se necessário
    localStorage.setItem('cart', JSON.stringify(cart));
});
