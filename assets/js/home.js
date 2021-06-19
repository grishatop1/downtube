var url = "";

function validateYouTubeUrl() {
    url = $('#link-input').val();
    if (url != undefined || url != '') {
        var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=|\?v=)([^#\&\?]*).*/;
        var match = url.match(regExp);
        if (match && match[2].length == 11) {
            setDataFormatTab("LOADING...", "Loading...", "")
            changePage("format");
            pywebview.api.newVideo(url).then(function(response) {
                setDataFormatTab(response[0], response[1], response[2])
            });
        }
    }
}

function downloadMP4() {
    changePage("download");
    pywebview.api.downloadVideo(url);
}

function downloadMP3() {
    changePage("download");
    pywebview.api.downloadAudio(url);
}