$("document").ready(function() {

    $.ajax({
        type: "POST",
        url: "http://localhost:8000/api/chart/",
        dataType: "json",
        traditional: true,

        data: {
            "input": "https://raw.githubusercontent.com/hvrc/reportsapi/master/_examples/_files/visits.csv",
            // "input": [],
            "type": "frequency",
            "cols": ["date_time", "full_name"],
            "width": 1200,
            "height": 300
        },

        success: function(response) {

            var chart = c3.generate({
                bindto: "#chartVisits",
                axis: {
                    x: {
                        type: "category",
                        categories: response.xTicks,
                        tick: { rotate: response.xTicksRotate, culling: false, centered: true, multiline: false },
                        label: { text: "Date" }
                    },
                    y: { label: { text: "Number of visits" } }
                },
                data: { json: response.json, type: "bar" },
                size: { width: response.width, height: response.height },
                title: { text: "Visits Report" },
                zoom: { enabled: false },
                point: { show: false },
                tooltip: { grouped: false },
                grid: { x: { show: false }, y: { show: true } },
                // color: { pattern: ["#1f77b4", "#aec7e8", "#ff7f0e", "#ffbb78", "#2ca02c", "#98df8a", "#d62728", "#ff9896", "#9467bd", "#c5b0d5", "#8c564b", "#c49c94", "#e377c2", "#f7b6d2", "#7f7f7f", "#c7c7c7", "#bcbd22", "#dbdb8d", "#17becf", "#9edae5"] }
            });
        }
    });
});
