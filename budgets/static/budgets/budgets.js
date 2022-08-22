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

function deleteBudgetItem(itemId) {
    let budgetItem = document.getElementById(`budget-item-${itemId}-row`);
    budgetItem.remove();
    return fetch(`/budgets/item/delete/${itemId}/`, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json',
            "Accept": "application/json"
        },
    })
}

function archiveBudget(budgetId) {
    let budget = document.getElementById(`budget-${budgetId}-table-row`);
    budget.remove();
    return fetch(`/budgets/archive/${budgetId}/`, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json',
            "Accept": "application/json"
        },
    })
}