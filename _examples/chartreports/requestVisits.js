$("document").ready(function() {

    $.ajax({
        type: "POST",
        url: "http://localhost:8000/api/chart/",
        dataType: "json",
        traditional: true,

        data: {
            "input": "/reportsapi/_examples/_files/visits.csv",
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
            });
        }
    });
});
