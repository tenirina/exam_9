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
        const imageId = $(this).data('image-id');
        let data = document.getElementsByClassName(imageId)[0];
        if (data.classList.contains('like')) {
            data.classList.remove('like');
            data.classList.add('dislike');
            data.value='Add to favorite'
            url = urlBase + `api/image/${imageId}/favorite/`;
            method = 'POST'
        } else {
            data.classList.remove('dislike')
            data.classList.add('like')
            data.value='Delete to favorite'
            url = urlBase + `api/image/${imageId}/not-favorite/`;
            method = 'DELETE'
        }
        $.ajax({
            url: url,
            method: method,
            headers: {'X-CSRFToken': getCookie('csrftoken')},
            success: function(response){

            },
            error: function(response){
                console.log(response)
                console.log('error')
            }
        })
    })
})