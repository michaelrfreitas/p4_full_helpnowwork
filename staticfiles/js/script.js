document.addEventListener("DOMContentLoaded", function () {

  const cards = document.querySelectorAll(".cards_single");

  function flipCard() {
    this.classList.toggle("flip");
  }
  cards.forEach((card) => card.addEventListener("click", flipCard));

});