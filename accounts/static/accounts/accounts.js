// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function updateBalance(accountId) {
    let balanceCell = document.getElementById(`${accountId}-balance`);
    balanceCell.contentEditable = true;
    balanceCell.focus();
    let editBalance = document.getElementById(`${accountId}-edit-balance`);
    editBalance.hidden = true;
    let saveBalance = document.getElementById(`${accountId}-save-balance`);
    saveBalance.hidden = false;
}

function saveBalance(accountId) {
    let balanceCell = document.getElementById(`${accountId}-balance`);
    balanceCell.contentEditable = false;
    balanceCell.blur();
    let editBalance = document.getElementById(`${accountId}-edit-balance`);
    editBalance.hidden = false;
    let saveBalance = document.getElementById(`${accountId}-save-balance`);
    saveBalance.hidden = true;
    return fetch(`/accounts/balance/update/${accountId}/${balanceCell.innerHTML}`, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json',
            "Accept": "application/json"
        },
    })
}