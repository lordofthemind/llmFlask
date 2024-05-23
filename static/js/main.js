$(document).ready(function () {
    $('#submitButton').click(function () {
        var userInput = $('#userInput').val();
        $.ajax({
            url: '/api/query',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ input: userInput }),
            success: function (response) {
                $('#responseText').text(response.response);
            },
            error: function (error) {
                $('#responseText').text('Error: ' + error.responseText);
            }
        });
    });

    $('#userInput').keypress(function (e) {
        if (e.which == 13) {
            $('#submitButton').click();
        }
    });
});
