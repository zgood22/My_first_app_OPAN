# My_first_app_OPAN
Unemployment data practiced 
## Setup

Create and activate a virtual environment:

```sh
conda create -n my-first-env python=3.10

conda activate my-first-env
```

Once in root:

```sh
Python app/my_script.py
```

OR (and we can now no longer run the unemployment the same way)

```sh
python -m app.unemployment
```

Install Packages:

```sh
pip install -r requirements.txt
```


THere is now an enviorment variable that uses the imput of "ALPHAVANTAGE_API_KEY"

You will also need to create a .env file and post the following variables
Obtain API Key from prof or from website
```sh

ALPHAVANTAGE_API_KEY="_______"
```

## Testing
Run tests:

NOTE** add a file called conftest.py to the root directory "conftest.py" which helps pytest find the file
```sh
pytest
```
In addition to the testing function imputted, the success of the application is verfied by automated testing.
Code has been refactored previously and should continue to be refactored if any significant changes are to be made

The name of the refactored weather app is called "weather2" to call the app:

```sh 
python -m app.weather2
```
