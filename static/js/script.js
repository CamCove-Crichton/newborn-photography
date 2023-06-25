console.log("Custom JavaScript file loaded");

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
