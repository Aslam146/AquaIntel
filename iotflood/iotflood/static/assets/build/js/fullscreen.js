document.addEventListener("DOMContentLoaded", function () {
    let fullscreenButton = document.getElementById("fullscreen-toggle");
    let fullscreenIcon = document.getElementById("fullscreen-icon");

    if (fullscreenButton) {
        fullscreenButton.addEventListener("click", toggleFullScreen);
    }

    function toggleFullScreen() {
        let elem = document.documentElement;

        if (!document.fullscreenElement) {
            if (elem.requestFullscreen) {
                elem.requestFullscreen();
            } else if (elem.mozRequestFullScreen) {
                elem.mozRequestFullScreen();
            } else if (elem.webkitRequestFullscreen) {
                elem.webkitRequestFullscreen();
            } else if (elem.msRequestFullscreen) {
                elem.msRequestFullscreen();
            }
            updateIcon(true);
        } else {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            } else if (document.mozCancelFullScreen) {
                document.mozCancelFullScreen();
            } else if (document.webkitExitFullscreen) {
                document.webkitExitFullscreen();
            } else if (document.msExitFullscreen) {
                document.msExitFullscreen();
            }
            updateIcon(false);
        }
    }

    function updateIcon(isFullscreen) {
        if (fullscreenIcon) {
            if (isFullscreen) {
                fullscreenIcon.classList.remove("glyphicon-fullscreen");
                fullscreenIcon.classList.add("glyphicon-resize-small");
            } else {
                fullscreenIcon.classList.remove("glyphicon-resize-small");
                fullscreenIcon.classList.add("glyphicon-fullscreen");
            }
        }
    }
});
