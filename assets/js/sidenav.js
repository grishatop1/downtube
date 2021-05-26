var navOpened = false;

var sideNode = document.getElementById("mySidenav")
var mainNode = document.getElementById("main")

function toggleNav() {
    if (!navOpened) {
        mainNode.style.marginLeft = "250px";
        sideNode.style.width = "250px";
        navOpened = true;
    } else {
        mainNode.style.marginLeft = "0px";
        sideNode.style.width = "0px";
        navOpened = false;
    }
}