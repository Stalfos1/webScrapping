function filterTable() {
    const input = document.getElementById("searchInput");
    const filter = input.value.toLowerCase();
    const table = document.querySelector(".styled-table");
    const rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName("td");
        if (cells.length >= 4) {
            const rank = cells[0].textContent.toLowerCase();
            const title = cells[1].textContent.toLowerCase();
            const score = cells[2].textContent.toLowerCase();
            const comments = cells[3].textContent.toLowerCase();

            if (rank.includes(filter) || title.includes(filter) || score.includes(filter) || comments.includes(filter)) {
                rows[i].style.display = "";
            } else {
                rows[i].style.display = "none";
            }
        }
    }
}