document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const donationId = urlParams.get('id');

    fetch(`/api/donations/${donationId}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('donor_name').value = data.donor_name;
            document.getElementById('email').value = data.email;
            document.getElementById('phone_number').value = data.phone_number;
            document.getElementById('collection_address').value = data.collection_address;
            document.getElementById('food_category').value = data.food_category;
            document.getElementById('quantity').value = data.quantity;
            document.getElementById('food_preparation_date').value = data.food_preparation_date;
            document.getElementById('special_note').value = data.special_note;
            document.getElementById('accept_terms').checked = data.accept_terms;
        });

    document.getElementById('editDonationForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = {
            donor_name: document.getElementById('donor_name').value,
            email: document.getElementById('email').value,
            phone_number: document.getElementById('phone_number').value,
            collection_address: document.getElementById('collection_address').value,
            food_category: document.getElementById('food_category').value,
            quantity: document.getElementById('quantity').value,
            food_preparation_date: document.getElementById('food_preparation_date').value,
            special_note: document.getElementById('special_note').value,
            accept_terms: document.getElementById('accept_terms').checked
        };

        fetch(`/api/donations/${donationId}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            window.location.href = '/donation_list.html';
        })
        .catch(error => console.error('Error:', error));
    });
});

