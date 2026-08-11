// Footer yili
document.querySelectorAll('[data-year]').forEach(function (el) {
  el.textContent = new Date().getFullYear();
});

// Mobil menu
var toggle = document.getElementById('mobileToggle');
var links = document.getElementById('navLinks');

if (toggle && links) {
  toggle.addEventListener('click', function () {
    var open = links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });

  links.addEventListener('click', function (event) {
    if (event.target.tagName === 'A') {
      links.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });
}
