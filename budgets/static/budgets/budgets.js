function addBudgetItem(budgetId) {
    let newRow = document.getElementById("add-budget-line-row");
    for (let i = 0; i < newRow.cells.length; i++) {
        let cell = newRow.cells[i];
        cell.innerHTML = "";
        cell.contentEditable = true;
    }
};