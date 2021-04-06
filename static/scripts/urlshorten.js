$(document).ready(function() {
    $("#submit").on("click", function() {
        var url = $("#url").val();

        $.ajax(url, {
            statusCode: {
                404: function() {
                    $("#url").val("");
                    $("#notfound-modal").modal('show');
                },
                200: function() {
                    $.ajax({
                        url: "https://www.0x0000.gq/shorten",
                        type: "POST",
                    
                        data: new FormData($("form")[0])
                    });
                }
            }
        });
    });
});