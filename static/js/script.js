// Assistance from Techie Delight
document.addEventListener("DOMContentLoaded", function () {
    console.log('Page is loaded');
});

// Assistance from code institutes I think therefore I blog walkthrough tutorials
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 5000);

// Assistance from ChatpGpt & Code Institutes JQuery events module
$(document).ready(function () {
    // Assistance from ChatGpt
    // Trigger modal to display upon click event
    $(document).on("click", ".deleteBtn", function () {
        console.log("Delete button clicked");
        var targetModal = $(this).attr("data-target-modal");
        $(targetModal).modal("show");
    });

    // A function to remove the active class and aria-current attribute and assign to clicked nav element
    $('.nav-link').click(function () {
        // Remove the active class from all navigation elements
        $('.nav-link').removeClass('active').removeAttr('aria-current');

        // Add the active class and set aria-current="page" to the clicked navigation element
        $(this).addClass('active').attr('aria-current', 'page');
    });

    // Show/hide the scroll-back-to-top button based on scroll position
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('#scrollBackToTopBtn').fadeIn();
        } else {
            $('#scrollBackToTopBtn').fadeOut();
        }
    });

    // Scroll to the top when button is clicked
    $('#scrollBackToTopBtn').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 'slow');
    });
});
