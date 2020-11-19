function send_request() {

    $.ajax({
        url: "send_sms.py",
        data: JSON.stringify(data),
        method: 'POST',
        contentType: 'application/json',
        success: function(data) {
            $('#request').replaceWith(data);
        }
    });
};