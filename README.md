# My_first_app_OPAN
Unemployment data practiced 
## Setup

Create and activate a virtual environment:

```sh
conda create -n my-first-env python=3.10

conda activate my-first-env
```

Install Packages:

```sh
pip install -r requirements.txt
```

## Usage
Once in root:

```sh
Python app/my_script.py
```

OR (and we can now no longer run the unemployment the same way)

```sh
python -m app.unemployment
```
See web app section 


THere is now an enviorment variable that uses the imput of "ALPHAVANTAGE_API_KEY"

You will also need to create a .env file and post the following variables
Obtain API Key from prof or from website
```sh

ALPHAVANTAGE_API_KEY="_______"
```

Running the stocks report
```sh
python -m app.stocks
```

## Testing
Run tests:

NOTE** add a file called conftest.py to the root directory "conftest.py" which helps pytest find the file
```sh
pytest
```
In addition to the testing function imputted, the success of the application is verfied by automated testing.
Code has been refactored previously and should continue to be refactored if any significant changes are to be made


## Web App

Run the web app (then view in the browser at http://localhost:5000/):
See more on the DEPLOY.md file

```sh
# Mac OS:
FLASK_APP=web_app flask run
```

The website can now be found at the url:
https://zgweb-app-2023.onrender.com/

In order to set up your own website, you will need to set up an account on render:
https://render.com/

you may need to install more requirements to get it to run since the local web abb
Check requirements.txt for all required packages


