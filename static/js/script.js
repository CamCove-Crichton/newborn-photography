// Assistance from Techie Delight
document.addEventListener("DOMContentLoaded", function () {
    console.log('Page is loaded');
});

// assistance from ChatGpt
// Function to call a modal to confirm a cancel or delete request
function deleteModal() {
    let deleteButtons = document.getElementsByClassName('deleteBtn');

    for (let deleteButton of deleteButtons) {
        deleteButton.addEventListener("click", function () {
            let modal = this.closest(".modal");
            $(modal).modal("show");
        });
    }
}

// Calling the delete modal function
deleteModal();