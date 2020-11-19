$('#review-form').on('submit', (evt) => {
    evt.preventDefault();
    
    // Get user's input from a form
    const formData = {
        rating: $('#rating-field').val(),
        review_date: $('#review-date-field').val()
        comment: $('#comment-field').val()
        submit: $('#submit-field').val()
    };

    //send form Data to the server(becomes a query string)
    $.get('/review-info.json', formData, (res) => {
        // display response from the server
        
    })
