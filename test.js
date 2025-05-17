let user_id, account_id;
const letters = new Set([563,522,123]);
let true_checker;

const errorMessage = document.getElementById("error-message");

document.getElementById("mySubmit").onclick = function() {
    user_id = document.getElementById("myid").value;
    user_id = Number(user_id);

    if (Number.isInteger(user_id) && user_id >= 100000) {
        console.log(user_id);
    }
};

document.getElementById("mySubmit1").onclick = function() {
    account_id = document.getElementById("bookid").value;
    account_id = Number(account_id);

       if (Number.isInteger(account_id)) {
        const found = letters.has(account_id); 
        if (found) {
            console.log("Found account ID:", account_id);
        } else {
            errorMessage.style.display = "block";
        }
    } else {
        console.log("Invalid input: not an integer.");
    }
    };