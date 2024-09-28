let slides = document.querySelectorAll('.slide');
let currentSlide = 0;
const nextButton = document.querySelector('.next');
const prevButton = document.querySelector('.prev');

// Função para mostrar o slide atual
function showSlide(index) {
    slides.forEach(slide => slide.classList.remove('active'));
    slides[index].classList.add('active');
}

// Função para avançar o slide automaticamente a cada 5 segundos
function autoSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

// Avançar manualmente
nextButton.addEventListener('click', () => {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
});

// Retroceder manualmente
prevButton.addEventListener('click', () => {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
});

// Iniciar com o primeiro slide
showSlide(currentSlide);

// Intervalo de 5 segundos para mudar o slide automaticamente
setInterval(autoSlide, 4000); // 5000 ms = 5 segundos
