const revealElements = document.querySelectorAll('.reveal');

const revealOnScroll = () => {
  const triggerPoint = window.innerHeight * 0.9;
  revealElements.forEach((el) => {
    const elementTop = el.getBoundingClientRect().top;
    if (elementTop < triggerPoint) {
      el.classList.add('visible');
    }
  });
};

window.addEventListener('scroll', revealOnScroll);
window.addEventListener('DOMContentLoaded', () => {
  revealOnScroll();
});
