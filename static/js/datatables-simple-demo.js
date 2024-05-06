function update_widgets(transactions, categories) {
    let category_obj = {};
    for (let category of categories) {
        category_obj[category.id] = category.name;
    }

    for (let transaction of transactions) {
        transaction.category = category_obj[transaction.category];
    }

    update_datatable(transactions);
}

function update_datatable(transactions) {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki
    window.datatable = new window.simpleDatatables.DataTable("#transaction-table", {
        data: {
            headings: Object.keys(transactions[0]),
            data: transactions.map(item => Object.values(item)),
        }
    })
}

fetch("http://127.0.0.1:8000/transactions/")
.then(response => response.json())
.then(
    data => {
    if (!data || !data.length) {
        return
    }
    let transactions = JSON.parse(JSON.stringify(data))
    fetch("http://127.0.0.1:8000/categories/")
    .then(response => response.json())
    .then(
        data => {
        if (!data || !data.length) {
            return
        }
        let categories = JSON.parse(JSON.stringify(data))
        update_widgets(transactions, categories);
    })
})