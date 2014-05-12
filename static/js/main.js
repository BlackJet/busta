function showModal(text) {
    var el = document.getElementById('overlay');
    el.style.visibility = (el.style.visibility == 'visible') ? 'hidden' : 'visible';
    document.body.style.overflow = 'hidden';
    el.children[0].innerHTML = text;

    el.onclick = function(){
        el.style.visibility = (el.style.visibility == 'visible') ? 'hidden' : 'visible';
        document.body.style.overflow = 'auto';
    }
}

function show($el){
    $el.css('visibility','visible');
}

function hide($el){
    $el.css('visibility','hidden');
}

function setUrl(){
    var login = $('input[name="login"]').val();
    var name = $('input[name="name"]').val();
    var oldValue = $('#url').html();
    var newValue = '<span>www.busta.cc/u/</span>' + login + '/' + name;
    if( oldValue == newValue) return;
    var regex = /^[a-z-_]+$/i;
    if (!login || !name || !regex.test(login) || !regex.test(name)) $('#url').html('');
    else $('#url').html(newValue);
}

var validate = function () {
    var regex = /^[a-z0-9_]+$/i;
    var valid = true;

    var $login = $('input[name="login"]');
    if (!regex.test($login.val())) {
        $login.siblings('label').removeClass('hidden');
        valid = false;
    }
    else $login.siblings('label').addClass('hidden');

    var $name = $('input[name="name"]');
    if (!regex.test($name.val())) {
        $name.siblings('label').removeClass('hidden');
        valid = false;
    }
    else $name.siblings('label').addClass('hidden');

    var $password = $('input[name="password"]');
    if (!$password.val()){
        $password.siblings('label').removeClass('hidden');
        valid = false;
    }
    else $password.siblings('label').addClass('hidden');

    return valid;
};

$(function () {

    if(document.getElementById('id')) show($('#modal-password'));

    setInterval(setUrl, 100);

    $('#submit').click(function () {
        var data = {};
        if (!validate()) return;
        data.text = $('#editor').html();
        data.login = $('input[name="login"]').val();
        data.name = $('input[name="name"]').val();
        data.password = $('input[name="password"]').val();


        $.ajax({
            url:'/add_post/',
            type:'post',
            data:data,
            success:function(response){
                if(response.success){
                    showModal('Paste saved.');
                    history.pushState(null, data.name, ['/u',data.login,data.name].join('/'));
                }
                else
                    showModal('Password is not correct. <br>Enter correct password or try with another page name or login.');
            }
        });
    });

    $('#password-form').submit(function(){
        return false;
    });

    $('#submit-password').click(function(){

        var action = $('#password-form').attr('action');
        var attrs = action.split('/');
        var data = {
            login:attrs[2],
            name:attrs[3]
        };
        data.password = $('input[id="open_password"]').val();
        if(!data.password) return;
        $.ajax({
            url:'/get_post/',
            type:'post',
            data:data,
            success:function(response){
                if(!response.success) return;
                hide($('#modal-password'));
                $('#editor').html(response.data.text);
            }
        })

    });

});