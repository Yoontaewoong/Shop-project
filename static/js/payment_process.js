$(function (){
    $('tbody > tr').on('mouseenter', function (event){
        $(this).addClass('myfocus')
    })
    $('tbody > tr').on('mouseleave', function (event){
        $(this).removeClass('myfocus')
    })

    $(document).on('click.cancel', 'button[name=btn-cancel]', function (){
        if (confirm('취소하시겠습니까?')){
            history.go(-1)
        }
        else {}
    })

    let total = 0;
    $('td.sum_result').each(function() {
        let price = $(this).prev().prev().attr('data-price');
        let multi_value = $(this).prev().attr('data-amount');
        let result = price * multi_value;
        $(this).text(result + " 원")
        total += result
    })
    $('.total_amount').text("총 구매 가격 : " + total + " 원")
})