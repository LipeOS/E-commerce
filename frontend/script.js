// Carrossel Script
let slides = document.querySelectorAll('.slide');
let currentSlide = 0;
const nextButton = document.querySelector('.next');
const prevButton = document.querySelector('.prev');

function showSlide(index) {
    slides.forEach(slide => slide.classList.remove('active'));
    slides[index].classList.add('active');
}

nextButton.addEventListener('click', () => {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
});

prevButton.addEventListener('click', () => {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
});

// Mostra o primeiro slide
showSlide(currentSlide);

// Script de Paginação
let currentPage = 1;
const totalPages = 5;
const prevPageButton = document.querySelector('.prev-page');
const nextPageButton = document.querySelector('.next-page');
const pageDisplay = document.querySelector('.paginacao span');

function updatePagination() {
    pageDisplay.textContent = `Página ${currentPage} de ${totalPages}`;
}

prevPageButton.addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        updatePagination();
    }
});

nextPageButton.addEventListener('click', () => {
    if (currentPage < totalPages) {
        currentPage++;
        updatePagination();
    }
});

updatePagination();
