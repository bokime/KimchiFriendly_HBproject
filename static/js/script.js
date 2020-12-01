// run request button to send message via Twilio API

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

    alert('Yay! Your request has been sent! Your maker will get back to you shortly.')

})