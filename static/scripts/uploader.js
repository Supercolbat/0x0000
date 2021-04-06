$(document).ready(function() {
    $("#file").on("change", function() {
        var f = this.files[0];

        if (f.size > 10 * 1024 * 1024) {
            $("#file").val("");
            $("#filetoolarge-modal").modal('show');
        }
    });
    
    $("#submit").on("click", function() {
        $.ajax({
            url: "https://www.0x0000.gq/upload",
            type: "POST",

            data: new FormData($("form")[0]),

            cache: false,
            contentType: false,
            processData: false,

            xhr: function() {
                var mXhr = $.ajaxSettings.xhr();
                if (mXhr.upload) {
                    mXhr.upload.addEventListener("progress", function(e) {
                        if (e.lengthComputable) {
                            $("progress").attr({
                                value: e.loaded,
                                max: e.total,
                            });
                        }
                    }, false);
                }
                return mXhr;
            }
        });
    });
});