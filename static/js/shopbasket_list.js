$(function (){
    $('tbody > tr').on('mouseenter', function (event){
        $(this).addClass('myfocus')
    })
    $('tbody > tr').on('mouseleave', function (event){
        $(this).removeClass('myfocus')
    })

    $(document).on('click.product_delete', 'button[name=product_delete]', function (){
        if (confirm("선택하신 상품을 삭제하시겠습니까?")){
            if ($("input:checkbox[data-check=list]:checked").length == 0){
                alert("선택된 상품이 없습니다.")
            }else {
            let check_Arr = [];

            $("input:checkbox[data-check=list]:checked").each(function (i){
                check_Arr.push($(this).val())
            })
            // alert(check_Arr)
             $.ajax({
               url : "/basket/delete/",
                type : 'POST',
                timeout : 3000,
                beforeSend: function (xhr, settings){
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
                    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    // Only send the token to relative URLs i.e. locally.
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                    }
                },
                data : {
                    'data[]': check_Arr
                },
                success : function () {
                    window.location.reload();
                },
                error : function (){
                    alert("문제가 발생했습니다. 문제 지속시 관리자에게 문의하세요")
                }
            });
            }
        }
        else {

        }
    });

    $(document).on('click.change_amount', 'button[name=change_amount]', function (){
            basket_id = $(this).attr('data-basket-id')
            amount_value = $("#"+basket_id).val()
            default_amount = $("#"+basket_id).attr('placeholder')

            if (amount_value == '' || amount_value == default_amount || amount_value < 0 ){

            }else if (amount_value != default_amount) {
                $.ajax({
               url : "/basket/update/",
                type : 'POST',
                timeout : 3000,
                beforeSend: function (xhr, settings){
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
                    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    // Only send the token to relative URLs i.e. locally.
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                    }
                },
                data : {
                    'id': basket_id,
                    'data': amount_value
                },
                success : function () {
                    window.location.reload();
                },
                error : function (){
                    alert("문제가 발생했습니다. 문제 지속시 관리자에게 문의하세요")
                }
            });
            }
    });

    let total = 0;
    $('td.sum_result').each(function() {
        let price = $(this).prev().prev().attr('data-price')
        let multi_value = $(this).prev().find("input").attr('placeholder')
        let result = price * multi_value;
        $(this).text(result + " 원")
        total += result
    })
    $('.total_amount').text("총 구매 가격 : " + total + " 원")
})