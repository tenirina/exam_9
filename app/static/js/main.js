let urlBase = 'http://localhost:8000/';

$(document).ready(function(){

   function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $('.favorite-btn').click(function(event){
        event.preventDefault();
        let input = $(this).find('favorite-btn');
        input.attr('disabled', true);
        const imageId = $(this).data('image-id');
        let data = document.getElementsByClassName(imageId)[0];
        if (data.classList.contains('like')) {
            data.classList.remove('like');
            data.classList.add('dislike');
            this.textContent = 'Delete to favorite'
            url = urlBase + `api/image/${imageId}/favorite/`;
            method = 'POST'
        } else {
            data.classList.remove('dislike')
            data.classList.add('like')
            this.textContent = 'Add to favorite'
            url = urlBase + `api/image/${imageId}/not-favorite/`;
            method = 'DELETE'
        }
        $.ajax({
            url: url,
            method: method,
            headers: {'X-CSRFToken': getCookie('csrftoken')},
            success: function(response){
                input = $(this).find('favorite-btn');
                input.attr('disabled', false);
            },
            error: function(response){
                console.log(response)
                console.log('error')
                input = $(this).find('favorite-btn');
                input.attr('disabled', false);
            }
        })
    })
})