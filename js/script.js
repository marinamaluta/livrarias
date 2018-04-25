// Inicio do JavaScript

(function($) {
    "use strict"; // Começo do "use strict"

    // JQuery para rolagem de página 
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top - 50)
        }, 1250, 'easeInOutExpo');
        event.preventDefault();
    });

    // Função para realçar o navegador superior quando a rolagem ocorrer
    $('body').scrollspy({
        target: '.navbar-fixed-top',
        offset: 51
    });

    // Função para fechar o menu responsivo e ao clicar o item
    $('.navbar-collapse ul li a').click(function(){ 
            $('.navbar-toggle:visible').click();
    });

    // Função para fechar a navegação
    $('#mainNav').affix({
        offset: {
            top: 100
        }
    })

})(jQuery);
 // Final do "use strict"

 // Inicio do JS do formulário

var fonte = document.querySelector('[data-contador-fonte]');
var inputs = document.querySelectorAll('#contactForm input');
var destino = document.querySelector('[data-contador-destino]');

for (var i = 0; i < inputs.length; i++) {
    var input = inputs[i];
    input.addEventListener('keydown', function() {
        this.parentNode.classList.remove('nao-toquei');
    })
}

fonte.addEventListener('keyup', function() {
  var digitado = fonte.value.length;
  var restante = 150 - digitado;
  destino.textContent = restante;
  this.parentNode.classList.remove('nao-toquei');
});

var formulario = document.querySelector('form');

formulario.addEventListener('submit', function(evento) {
  evento.preventDefault();
  if(this.checkValidity() == true) {
    alert('Obrigada pelo seu contato! Qualquer dúvida, entre em contato diretamente pelo tel (11) 9999-9999');
  } else {
    alert('Preencha todos os campos corretamente')
  }
});


// FInal do JS do formulário

// Final do JavaScript
