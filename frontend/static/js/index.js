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
