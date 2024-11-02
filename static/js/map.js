// Function to handle form submission
document.addEventListener('DOMContentLoaded', (event) => {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (e) {
        e.preventDefault(); // Prevent the default form submission

        const locationInput = document.getElementById('location').value;
        
        // You can add more JavaScript functionality here as needed
        console.log('Location submitted:', locationInput);

        // Optionally, if you want to show a message or do something else
        alert(`Predicting landslide for location: ${locationInput}`);
        
        // Submit the form programmatically if you want
        this.submit(); 
    });
});
