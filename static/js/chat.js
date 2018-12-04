$('#Chat-form').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        type : 'POST',
        url : $(this).attr("action"),
        data : {
            message : $('#chat-msg').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },
        success : function(json){
            console.log(json);
            $('#chat-msg').val('');
            $('#emptyerror').remove();
            $('#msg-list').append('<div class="container2 darker">' +
                                    '<img class="right" src="https://upload.wikimedia.org/wikipedia/commons/d/d3/User_Circle.png" alt="Avatar" style="width:100%;">' +
                                    '<p>' + json.msg + '</p>' +
                                    '<span class="time-right">' + json.user + '</span> </div>');
        }
    });
});

function getMessages(id){
        var url = '/messages/' + id;
        console.log(url);

        $.get(url, function(messages){
            console.log(messages);
            $('#msg-list').html(messages);
        });
    }

$(document).ready(function() {
    $('form input').keyup(function() {

        var empty = false;
        $('form  input').each(function() {
            if ($(this).val() == '') {
                empty = true;
            }
        });

        if (empty) {
            $('#register').attr('disabled', 'disabled'); // updated according to http://stackoverflow.com/questions/7637790/how-to-remove-disabled-attribute-with-jquery-ie
        } else {
            $('#register').removeAttr('disabled'); // updated according to http://stackoverflow.com/questions/7637790/how-to-remove-disabled-attribute-with-jquery-ie
        }
    });
});

$(document).ready(function() {
     $('#register').attr('disabled','disabled');
     $('#chat-msg').keyup(function() {
        if($(this).val() != '') {
            $('#register').removeAttr('disabled');
        }
        else {
            $('#register').attr('disabled','disabled');
        }
     });
});

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|sOPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});