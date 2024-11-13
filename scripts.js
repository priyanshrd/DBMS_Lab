document.getElementById("addAccidentForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const reportNumber = document.getElementById("report_number").value;
    const date = document.getElementById("date").value;
    const location = document.getElementById("location").value;

    fetch("/add-accident", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ report_number: reportNumber, date: date, location: location })
    }).then(response => response.json())
      .then(data => {
          alert("Accident added successfully!");
      })
      .catch(error => {
          console.error("Error:", error);
          alert("Failed to add accident.");
      });
});

function fetchReports() {
    fetch("/get-reports")
        .then(response => response.json())
        .then(data => {
            const reportsDiv = document.getElementById("reports");
            reportsDiv.innerHTML = "<h3>Accident Reports:</h3>";
            data.forEach(report => {
                const reportEntry = document.createElement("div");
                reportEntry.textContent = `Report Number: ${report.report_number}, Date: ${report.date}, Location: ${report.location}`;
                reportsDiv.appendChild(reportEntry);
            });
        })
        .catch(error => console.error("Error fetching reports:", error));
}
