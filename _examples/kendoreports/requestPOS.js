$("document").ready(function() {

    $.ajax({
        type: "POST",
        url: "http://localhost:8000/api/kendo/",
        dataType: "json",
        traditional: true,

        data: {
            "input": "/Users/Harsh/Desktop/reportsapi/_examples/_files/pos.csv",
            // "input": [],
            "type": "",
            "cols": ["Date", "Amount"],
            "width": 1200,
            "height": 300
        },

        success: function(response) {

            var series = [];
            for (var i = 0; i < response.columns.length; i++) {
                series.push({
                    name: response.columns[i],
                    field: response.columns[i],
                    type: "line",
                    style: "smooth",
                    markers: { visible: false }
                });
            }

            $("#kendoPOS").kendoStockChart({
                dataSource: { data: response.data },
                chartArea: { width: response.width, height: response.height },
                series: series,
                dataField: "date",

                categoryAxis: {
                    title: { text: "Date" },
                    majorGridLines: { visible: true },
                    // baseUnit: "months",
                    // baseUnitStep: 0
                },

                valueAxis: {
                    title: { text: "Amount" },
                    labels: { template: "#=  kendo.toString(value, '0,.0;(0,.0)') # " + "INR"}
                },

                title: { text: "POS Report (3 Years)" },
                legend: { visible: true, position: "bottom" },
                navigator: { visible: false, series: { field: "value" } },
                tooltip: { visible: true, background: "white", border: { width: 2 } }
            });
        }
    });
});
