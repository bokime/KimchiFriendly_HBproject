$('#request-btn').on('click', () => {
    
    $.ajax({
        url: "/KimchiFriendly/send_sms.py",
        success: function(response) {
            alert('Your request has been sent!')
        }
    })
    // alert('Your request has been sent!')
    //run send_sms.py
})



// //OR
// $.ajax({
//     url: "/KimchiFriendly/send_sms.py",
//     success: function(response) {
//         alert('Your request has been sent!')
//     }
// })

// function goPython(){
//     $.ajax({
//         url: "/send_sms.py",
//         context: document.body
//     }).done(function() {
//         alert('finished python script');;
//     });
// }

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