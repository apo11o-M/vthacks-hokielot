{% comment %} document.addEventListener("DOMContentLoaded", function() {
    // Simulated available parking spaces
    let availableSpaces = 21;

    // Update the UI
    document.getElementById("available-spaces").textContent = availableSpaces;
    const progressBar = document.getElementById("progress-bar");
    progressBar.value = 62 - availableSpaces;

    // Dropdown to change parking lot names
    const otherLotsDropdown = document.getElementById("other-lots");
    otherLotsDropdown.addEventListener('change', function() {
        document.getElementById("parking-lot-name").textContent = this.value;
    });
}); {% endcomment %}
