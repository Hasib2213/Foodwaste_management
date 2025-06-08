// Inventory Management
document.getElementById('inventoryForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const itemName = document.getElementById('itemName').value;
    const expiryDate = document.getElementById('expiryDate').value;

    // Add item to the list
    const item = document.createElement('div');
    item.className = "list-group-item";
    item.textContent = `${itemName} - Expires on: ${expiryDate}`;
    document.getElementById('inventoryList').appendChild(item);

    // Clear form
    document.getElementById('inventoryForm').reset();
});

// Donation Matching
document.getElementById('findCharities').addEventListener('click', function () {
    fetch('/api/charities/')
        .then(response => response.json())
        .then(data => {
            const charityList = document.getElementById('charityList');
            charityList.innerHTML = '';
            data.forEach(charity => {
                const charityItem = document.createElement('div');
                charityItem.className = "list-group-item";
                charityItem.textContent = `${charity.name} - ${charity.location}`;
                charityList.appendChild(charityItem);
            });
        });
});




//for alert



document.addEventListener("DOMContentLoaded", function() {
    fetch('/api/inventory/')
    .then(response => response.json())
    .then(data => {
        let today = new Date();
        data.forEach(item => {
            let expiryDate = new Date(item.expiry_date);
            let diff = Math.ceil((expiryDate - today) / (1000 * 60 * 60 * 24));

            if (diff <= 3) {
                alert(`Alert: ${item.name} is expiring in ${diff} days!`);
            }
        });
    });
});
