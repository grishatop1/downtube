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