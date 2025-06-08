document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("donationForm").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent default form submission

        let formData = {
            donor_name: document.getElementById("donor_name").value,
            email: document.getElementById("email").value,
            phone_number: document.getElementById("phone_number").value,
            collection_address: document.getElementById("collection_address").value,
            food_category: document.getElementById("food_category").value,
            quantity: document.getElementById("quantity").value,
            food_preparation_date: document.getElementById("food_preparation_date").value,
            special_note: document.getElementById("special_note").value,
            accept_terms: document.getElementById("accept_terms").checked ? "on" : "off"
        };

        fetch("/Vsub/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken") // CSRF protection
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert("Donation submitted successfully!");
                window.location.reload(); // Refresh after submission
            } else {
                alert("Error: " + data.error);
            }
        })
        .catch(error => console.error("Error:", error));
    });

    // Function to get CSRF Token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            let cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                if (cookie.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
