document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/donations/')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#donationTable tbody');
            data.forEach(donation => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${donation.donor_name}</td>
                    <td>${donation.email}</td>
                    <td>${donation.phone_number}</td>
                    <td>${donation.collection_address}</td>
                    <td>${donation.food_category}</td>
                    <td>${donation.quantity}</td>
                    <td>${donation.food_preparation_date}</td>
                    <td>${donation.special_note}</td>
                    <td>
                        <button onclick="editDonation(${donation.id})">Edit</button>
                        <button onclick="deleteDonation(${donation.id})">Delete</button>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        });
});

function editDonation(id) {
    window.location.href = `/edit_donation.html?id=${id}`;
}

function deleteDonation(id) {
    fetch(`/api/donations/${id}/`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => {
        if (response.ok) {
            window.location.reload();
        }
    })
    .catch(error => console.error('Error:', error));
}

