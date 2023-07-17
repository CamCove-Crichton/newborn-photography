// Assistance from Techie Delight
document.addEventListener("DOMContentLoaded", function () {
    console.log('Page is loaded');
});

// assistance from ChatGpt
// Function to call a modal to confirm a cancel or delete request
function deleteModal(targetModal) {
    let deleteButtons = document.getElementsByClassName("deleteBtn");

    for (let deleteButton of deleteButtons) {
        deleteButton.addEventListener("click", handleDeleteButtonClick.bind(null, targetModal), { once: true });
    }

    function handleDeleteButtonClick(targetModal) {
        console.log("Delete button clicked");
        let modal = document.querySelector(targetModal);
        $(modal).modal("show");
    }
}

// Assistance from code institutes I think therefore I blog walkthrough tutorials
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 5000);

// Assistance from ChatpGpt & Code Institutes JQuery events module
$(document).ready(function () {
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