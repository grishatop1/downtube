function validateYouTubeUrl() {
    var url = $('#link-input').val();
    if (url != undefined || url != '') {
        var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=|\?v=)([^#\&\?]*).*/;
        var match = url.match(regExp);
        if (match && match[2].length == 11) {
            // Do anything for being valid
            // if need to change the url to embed url then use below line
            //$('#link-input').attr('src', 'https://www.youtube.com/embed/' + match[2] + '?autoplay=0');
            console.log("Valid url! :D")
            changePage("format");
            pywebview.api.reqInfo(url);
        }
        else {
            console.log("BAD URL!")
        }
    }
}