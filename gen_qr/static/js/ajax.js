function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
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
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


//　base64のHTML imgタグへの反映用に必要！
function b64toBlob(b64Data, contentType, sliceSize = 512) {
    const byteCharacters = atob(b64Data);
    const byteArrays = [];
    for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
      const slice = byteCharacters.slice(offset, offset + sliceSize);
      const byteNumbers = new Array(slice.length);
      for (let i = 0; i < slice.length; i++) {
        byteNumbers[i] = slice.charCodeAt(i);
      }
      const byteArray = new Uint8Array(byteNumbers);
      byteArrays.push(byteArray);
    }
    const blob = new Blob(byteArrays, { type: contentType });
    return blob;
  }


// 単一formに複数のsubmitを用意するときに使う
// フォームにtype="hidden"のinput要素を追加
$('#create_ajax').append('<input name="key" type="hidden" value="" />');
// ボタンクリック時、上記で追加したtype="hidden"のinput要素にクリックした要素のvalを設定
$("#btn1, #btn2").click(function(){
    $('input[name=key]').val($(this).val());
});

$('#create_ajax').on('submit', function(e) {
    e.preventDefault();
    // 押されたボタンによる切り分け
    console.log("押されたボタンは: " + $('input[name=key]').val())
    if($('input[name=key]').val() == 'QR発行'){
        console.log("QRコード発行用のdata登録")
        var data = {
            'get_url': $('#get_url').val(),
            'get_usage': $('#get_usage').val(),
            'get_explain': $('#get_explain').val(),
            'get_flg_shorturl':$('#get_flg_shorturl:checked').val(),
            'create_mode': 'create',
        };
        console.log({data})
    }else if($('input[name=key]').val() == '登録'){
        console.log("DB登録用のdata登録")
        var data = {
            'get_url': $('#get_url').val(),
            'get_usage': $('#get_usage').val(),
            'get_explain': $('#get_explain').val(),
            'get_flg_shorturl':$('#keyURL').text(),
            'create_mode': 'regist',
            //'im_base64':$(".result_qr"),
        };
        console.log({data})
    }
        
    $.ajax({
        'url': '/gen_qr/create/create_ajax/',
        'type': 'POST',
        //'contentType': 'False',
        //'processData': 'False',
        'data': data,
        'dataType': "json"
    })
    .done(function(response){
        console.log("done!!");
        //$('.result_qr').prepend('<p>表示画像のURL：' + response.path_id + '</p>');
        if(response.error_flag==1){
            console.log("QR生成出来ませんでした。")
            $('#regist_response').text("URLを設定し直してください")
            //$('#regist_response').text("")
            //$('#keyURL').css("color","#ff0000")
        } else if(response.error_flag==2){
            console.log("そのURLはすでに登録されています")
        } else {
            $('#keyURL').text('元URL: ' + response.URL)
            $('#regist_response').text("")
            //$('#keyURL').css("color","#1100ff")
        }

        let blob = b64toBlob(response.qr, "image/png");
        console.log({blob});
        let imgUrl = URL.createObjectURL(blob);
        $('.result_qr').get(0).src = imgUrl;

        if(!response.URL){
            $('#regist_response').text("登録失敗");
            $('#regist_response').css('color','#1100ff');
        } else if(response.create_mode=="regist"){
            $('#regist_response').text("登録完了!");
            $('#regist_response').css('color','#ff0000');
        } else if(response.create_mode=="create"){
            if(response.error_flag==0){
                $('#regist_response').text("生成完了!");
                $('#regist_response').css('color','#20b100');
            } else if(response.error_flag==2) {
                $('#regist_response').text("このURLは登録済です");
                $('#regist_response').css('color','#1100ff');
            };
        };
    })

    // ↓ここでAjax処理に失敗した場合にコンソールにlogを出力するように設定している。
    .fail(function(jqXHR, textStatus, errorThrown) {
        console.log('Fail-Error!');
        console.log(jqXHR);
        console.log(textStatus);
        console.log(errorThrown);
        alert("error！");
    })
    //.always(function() {
    //    console.log("always");
    //})
});

