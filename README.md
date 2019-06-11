# reportsapi

# About
Reportsapi contains three apps: csvreport, chartreport and kendoreport.
[about the apps, why they exist, kendo especially]

## Frequency report

[about frequency reports, how they work, give short example maybe]

```json
{
	"input": "path/to/file.csv",
	"type": "frequency",
	"cols": ["", ""]
}
```

[explain each key value]

## Creating a table of the specified columns

[how this works]

```json
{
	"input": "path/to/file.csv",
	"type": "frequency",
	"cols": ["", ""]
}
```

[explain each key value]

---
# Run locally

Clone
```bash
$ git clone "https://github.com/hvrc/reportsapi.git"
$ cd reportsapi
```

Create a virtualenv & activate it
```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

Install requirements
```bash
$ pip install -r requirements.txt
```

Run
```bash
$ python manage.py runserver
```

## View the examples

Open a new terminal tab,
```bash
$ cd _examples
$ python -m SimpleHTTPServer 8001
```

Open [localhost:8000](http://127.0.0.1:8000) in your browser and view the examples

---
# Examples
[where examples are located, why they exist]

### Example CSV Report (Visits Data)

[about input]

![visits input csv image]("")

[about post req, how to send]

```
POST http://127.0.0.1:8000/api/csv
```
```json
{
	"input": "path/to/visits.csv",
	"type": "frequency",
	"cols": ["date_time", "full_name"]
}
```
[how to save output in postman, nature of output]

![visits output csv image]("")

### Example CSV Report (Inflow Data)

[about input]

![visits input csv image]("")

[about post req]

```
POST http://127.0.0.1:8000/api/csv
```
```json
{
	"input": "path/to/visits.csv",
	"type": "detach",
	"cols": ["payment_date", "outstanding_principal_opening_balance", "outstanding_principal_closing_balance"]
}
```
[similar to prev]

![inflow output csv image]("")

### Example Chart Report (Visits Data)

[about input]

![inflow input csv image]("")

[about post req, how to send, how ajax works, how that script works]
[width height]

```javascript
$("document").ready(function() {

    $.ajax({
        type: "POST",
        url: "http://localhost:8000/api/chart/",
        dataType: "json",
        traditional: true,

        data: {
            "input": "path/to/visits.csv",
            // "input": [],
            "type": "frequency",
            "cols": ["date_time", "full_name"],
            "width": 1200,
            "height": 300
        },

        success: function(response) {

            var chart = c3.generate({
                ...
            });
        }
    });
});

```
[about output]

![visits output chart image]("")

### Example Chart Report (Inflow Data)

[about input]

![inflow input csv image]("")

[similar to prev]

```javascript
$("document").ready(function() {

    $.ajax({
        type: "POST",
        url: "http://localhost:8000/api/chart/",
        dataType: "json",
        traditional: true,

        data: {
            "input": "/reportsapi/_examples/_files/inflow.csv",
            // "input": [],
            "type": "detach",
            "cols": ["payment_date", "outstanding_principal_opening_balance", "outstanding_principal_closing_balance"],
            "width": 1200,
            "height": 300
        },

        success: function(response) {

            var chart = c3.generate({
                ...
            });
        }
    });
});
```

[about output]

![inflow output chart image]("")

### Example Kendo Report

[why does kendo exist, nature of input]

![pos input csv image]("")

[about req]
[about series]

```javascript
$("document").ready(function() {

    $.ajax({
        type: "POST",
        url: "http://localhost:8000/api/kendo/",
        dataType: "json",
        traditional: true,

        data: {
            "input": "path/to/pos.csv",
            // "input": [],
            "type": "detach",
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
                ...
            });
        }
    });
});

```

[about output]

![pos output chart image]("")

---
