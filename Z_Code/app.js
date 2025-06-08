const API_BASE_URL = 'http://127.0.0.1:8000/api';

// Fetch and display food items
async function fetchFoodItems() {
    const response = await fetch(`${API_BASE_URL}/food-items/`);
    const data = await response.json();
    const foodList = document.getElementById('food-list');
    foodList.innerHTML = data.map(item => `
        <li>
            ${item.name} - ${item.quantity} units (Expires: ${item.expiry_date})
            <button onclick="recordWaste(${item.id})">Record Waste</button>
            <button onclick="donateFood(${item.id})">Donate</button>
        </li>
    `).join('');
}

// Add a new food item
document.getElementById('food-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = {
        name: document.getElementById('name').value,
        quantity: document.getElementById('quantity').value,
        expiry_date: document.getElementById('expiry-date').value,
        location: document.getElementById('location').value,
    };
    await fetch(`${API_BASE_URL}/food-items/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
    });
    fetchFoodItems();
});

// Record waste
async function recordWaste(foodItemId) {
    const wastedQuantity = prompt('Enter wasted quantity:');
    if (wastedQuantity) {
        await fetch(`${API_BASE_URL}/waste-records/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ food_item: foodItemId, wasted_quantity: wastedQuantity, reason: 'Overstock' }),
        });
        fetchFoodItems();
    }
}

// Donate food
async function donateFood(foodItemId) {
    const donatedTo = prompt('Enter recipient organization:');
    const donatedQuantity = prompt('Enter donated quantity:');
    if (donatedTo && donatedQuantity) {
        await fetch(`${API_BASE_URL}/donations/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ food_item: foodItemId, donated_to: donatedTo, donated_quantity: donatedQuantity }),
        });
        fetchFoodItems();
    }
}

// Initial fetch
fetchFoodItems();