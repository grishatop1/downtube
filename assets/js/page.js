var degree = 0;
var currentPage = "link";
const types = {
    "link": 0,
    "format": 1,
    "download": 2
}

function rotateWheelTo(type) {
    degree = types[type] * 30
    document.getElementById("wheel").style.transform = "translateY(-50%) rotate("+degree+"deg)"
}

function changePage(type) {
    var percent = -types[type] * 100;
    var scrollerNode = document.getElementsByClassName("scroller")[0];

    $(".page").css("transform", "scale(0.84)")
    
    rotateWheelTo(type);
    scrollerNode.style.filter = "blur(1.5px)"
    scrollerNode.style.top = percent + "%"
    setTimeout(function() {
        scrollerNode.style.filter = ""
        $(".page").css("transform", "")
    }, types[type]+1*700);
}

function setDataFormatTab(title, desc, thumbnail_url) {
    $(".info-title").html(title)
    $(".info-desc").html(desc)
    $(".info-thumb img").attr("src", thumbnail_url)
}

function setProgressBarWidth(percent) {
    document.getElementById("down-progress").style.width = percent + "%";
}

function setProgressText(text) {
    $(".downloading h3").html(text)
}

function setDownloaded() {
    $(".downloading").css("display", "none")
    $(".downloaded").css("display", "flex")
}

function resetDownloaded() {
    $(".downloaded").css("display", "none")
    $(".downloading").css("display", "flex")
}

function reset() {
    setDataFormatTab("LOADING...", "Loading...", "")
    $("#link-input").val("")
    setProgressBarWidth(0)
    setProgressText("LOADING...")
    changePage("link")
    setTimeout(function() {
        resetDownloaded()
    }, 500)
}

function setVideoNotFound() {
    setDataFormatTab(
        "Video not found :/",
        "Maybe it is also problem with your internet connection, idk...",
        "")
}