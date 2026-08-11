// Footer yili
document.querySelectorAll('[data-year]').forEach(function (el) {
  el.textContent = new Date().getFullYear();
});

// Ic linklerde yumusak kaydirma
document.querySelectorAll('a[href^="#"]').forEach(function (link) {
  link.addEventListener('click', function (event) {
    var target = document.querySelector(link.getAttribute('href'));
    if (!target) return;
    event.preventDefault();
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});
