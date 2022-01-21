# Optimus
## Documentation

### API Endpoint
```
GET /api/trains
```

### Response body schema

```json
{
"train_number": "Train number",
"train_numbering_system": "Train numbering system: a train numbering system allocates number ranges (for the train numbers) to train types or train categories, as well as to individual lines.",
"transport_period": "Transport period - on which days the train runs --> referenced in the annual formation (annual formation (transport period)) Bitmap which defined on which days the train runs in the timetable version.",
"debtor_code": "The debtor code identifies the railway undertakings and is an instrument for clearing.",
"train_type": "Train type according to timetable",
"suffix": "Train number affix, e.g. R for Rangierfahrt (shunting movement).",
"traction": "Indicates whether the vehicle is running in a multiple unit.",
"from_station": "Departure station",
"uic": "UIC country code of departure station (CH = 85)",
"departure_time": "Time of departure at the departure station",
"to_station": "Arrival station",
"arrival_time": "Time of arrival at the arrival station",
"rotation": "A rotation is the scheduling of one or more traction units or coaches (groups), which are used for one or a series of operations during n days.",
"rotation_start_time": "Duration of service; a rotation can have several different validities within one timetable version. From = valid from",
"rotation_end_time": "Duration of service; a rotation can have several different validities within one timetable version. By= Valid until",
"daily_runs": "Total of all trains run with the planned vehicle within one day",
"daily_runs_transport_period": "Daily runs for the transport period",
"nb_runs_on_monday": "Number of runs on mondays",
"nb_runs_on_tuesday": "Number of runs on tuesdays",
"nb_runs_on_wednesday": "Number of runs on wednesdays",
"nb_runs_on_thursday": "Number of runs on thursdays",
"nb_runs_on_friday": "Number of runs on fridays",
"nb_runs_on_saturday": "Number of runs on saturdays",
"nb_runs_on_sunday": "Number of runs on sundays",
"block_designation": "Vehicles are put together into a formation in a block.  The block is defined for each rotation. Refers to the rolling stock list",
"transport_period_c": "Transport period of the train (Column C)",
"daily_runs_r": "Daily runs (Column R)",
"bitmap": "For each day of the timetable period, there is a character in the Bitmap x  the train runs on this day -  the train does not run on this day.",
"timetable_period_start": "When the timetable period or bitmap starts"
}
```

## Get Started 

First install the dependancies
```sh
pip install -r requirements.txt
```

### On ``Linux``

To create a virtual python environnment :

```sh
python3 -m venv venv

. venv/bin/activate

export FLASK_APP=app.py
export FLASK_ENV=development
python -m flask run
```

## On ``Windows`` with ``Powershell``

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
