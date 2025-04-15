$(document).ready(function () {
    // Initialize Bootstrap 5 Tooltip
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Check if dark mode is enabled in localStorage
    if (localStorage.getItem("dark-mode") === "enabled") {
        $("body").addClass("dark-mode");
        $("#darkModeIcon").removeClass("fa-moon").addClass("fa-sun");
    }

    // Dark Mode Toggle
    $("#darkModeToggle").click(function () {
        $("body").toggleClass("dark-mode");

        // Change icon
        if ($("body").hasClass("dark-mode")) {
            $("#darkModeIcon").removeClass("fa-moon").addClass("fa-sun");
            localStorage.setItem("dark-mode", "enabled");
        } else {
            $("#darkModeIcon").removeClass("fa-sun").addClass("fa-moon");
            localStorage.setItem("dark-mode", "disabled");
        }
    });
});