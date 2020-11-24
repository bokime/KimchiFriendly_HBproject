$('#request-btn').on('click', (evt) => {
    evt.preventDefault();

    console.log(evt.target)

    const url = $('#url_for_sender_request').val()
        console.log(url)

    const maker_id = $('#maker_id').val()
        console.log(maker_id)
    
    $.get(url, {maker_id:maker_id}, (res) => {
        console.log(res)
    })

    alert('Your request has been sent!')

})




// pagination
// $(document).ready(function(){
//     $('#share-detail').after('<div id="nav"></div>');
//     var rowsShown = 4;
//     var rowsTotal = $('#share-detail tbody tr').length;
//     var numPages = rowsTotal/rowsShown;
//     for(i = 0;i < numPages;i++) {
//         var pageNum = i + 1;
//         $('#nav').append('<a href="#" rel="'+i+'">'+pageNum+'</a> ');
//     }
//     $('#share-detail tbody tr').hide();
//     $('#share-detail tbody tr').slice(0, rowsShown).show();
//     $('#nav a:first').addClass('active');
//     $('#nav a').bind('click', function(){

//         $('#nav a').removeClass('active');
//         $(this).addClass('active');
//         var currPage = $(this).attr('rel');
//         var startItem = currPage * rowsShown;
//         var endItem = startItem + rowsShown;
//         $('#share-detail tbody tr').css('opacity','0.0').hide().slice(startItem, endItem).
//                 css('display','table-row').animate({opacity:1}, 300);
//     });
// });



// $('#review-form').on('submit', (evt) => {
//     evt.preventDefault();
    
//     // Get user's input from a form
//     const formData = {
//         rating: $('#rating-field').val(),
//         review_date: $('#review-date-field').val(),
//         comment: $('#comment-field').val(),
//         submit: $('#submit-field').val()
//     };

//     //send form Data to the server(becomes a query string)
//     $.get('/review-info.json', formData, (res) => {
//         // display response from the server
//         alert('Your review has been submitted!')
//     })