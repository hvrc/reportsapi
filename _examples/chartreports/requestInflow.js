$("document").ready(function() {

    $.ajax({
        type: "POST",
        url: "http://localhost:8000/api/chart/",
        dataType: "json",
        traditional: true,

        data: {
            "input": "/Users/Harsh/Coding/Projects/Gromor/Reports/reportsapi/_examples/_files/inflow.csv",
            // "input": ["localhost", "root", "hvrc2000$", "ReportsDB", 3306, "inflow"],
            "type": "detach",
            "cols": ["payment_date", "outstanding_principal_opening_balance", "outstanding_principal_closing_balance"],
            "width": 1200,
            "height": 300
        },

        success: function(response) {

            var chart = c3.generate({
                bindto: "#chartInflow",
                axis: {
                    x: {
                        type: "category",
                        categories: response.xTicks,
                        tick: { rotate: response.xTicksRotate, culling: false, centered: true, multiline: false },
                        label: { text: "Date" }
                    },
                    y: { label: { text: "Amount (in INR)" } }
                },
                data: { json: response.json, type: "spline" },
                size: { width: response.width, height: response.height },
                title: { text: "Inflow (POS) Report" },
                zoom: { enabled: false },
                point: { show: false },
                tooltip: { grouped: false },
                grid: { x: { show: false }, y: { show: true } },
            });
        }
    });
});
