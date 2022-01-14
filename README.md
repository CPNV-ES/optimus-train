# Optimus
## Documentation

### API Endpoint
```
GET /api/trains
```

### Response body schema

```json
{
"manufacturer" : "string",
"constructed" : "string",
"start_service" : "string",
"end_service" : "string",
"car" : "number",
"capacity" : "number",
"capacity_first" : "number",
"capacity_second" : "number",
"operator" : "string",
"name" : "string",
"length_m" : "number",
"width_mm" : "number",
"height_mm" : "number",
"max_speed" : "number",
"weight_t" : "number",
"motor_type" : "string",
"power_output_ac" : "number",
"power_output_dc" : "number",
"tractive_force" : "number",
"electric_system" : "string",
"current_collection" : "string",
"uic_classification" : "string",
"track_gauge_mm :" : "number"
}
```

> Note : This is an example of what data could be returned

## Get Started 

First install the dependancies
```sh
pip install -r requirements.txt
```

### On Linux

To create a virtual python environnment :

```sh
python3 -m venv venv

. venv/bin/activate

export FLASK_APP=app.py
export FLASK_ENV=development
python -m flask run
```

## On Windows with Powershell

```powershell
python -m venv venv

. .\venv\Scripts\Activate.ps1

$Env:FLASK_APP="app.py"
$Env:FLASK_ENV="development"
python -m flask run
```

Alternatively you can also do this on Windows if the solution above didn't worked
```powershell
python -m venv venv

.\venv\Scripts\activate

$set FLASK_APP=app.py
$set FLASK_ENV=development
python -m flask run
```

This launches a very simple builtin server, which is good enough for testing but probably not what you want to use in production.

If you enable debug support the server will reload itself on code changes, and it will also provide you with a helpful debugger if things go wrong.

If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding
--host=0.0.0.0 to the command line:

```sh
flask run --host=0.0.0.0
```
