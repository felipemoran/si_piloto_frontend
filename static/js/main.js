$(function() {

  console.log('Main.js loaded')

  $( document ).ready(function() {
    $('#form_comentario').on('submit', function(event){
      console.log('Clicou!!!')
      comentario_ajax()
      event.preventDefault();
    })
  });

  function comentario_ajax(){

    $.ajax({
      url: '/comentar_post/',
      type: 'POST',

      data : {
        csrfmiddlewaretoken: csrf_token,
        comentario: $('#texto_comentario').val(),
        post_id: post_id
      },

      success: function(data) {
        if (data['status'] == 'OK') {
          adiciona_comentario($('#texto_comentario').val())
          $('#texto_comentario').val('')
        }
        else {
          console.log("A resposta não foi OK")
        }
      },

      error: function(data){
        console.log("Alguma coisa errada aconteceu com o comentario")
      }
    })
  }

  function adiciona_comentario(texto) {
    $('#pagina').append(
      '<div class="media">\
        <a class="pull-left" href="#">\
              <img class="media-object" src="http://placehold.it/64x64" alt="">\
          </a>\
          <div class="media-body">\
              <h4 class="media-heading">'+nome_usuario+'\
              </h4>'+texto+'</div>\
      </div>')
    $('#form_comentario').val("")
  }


})


