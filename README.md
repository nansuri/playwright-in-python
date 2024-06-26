# Play-In-Pom
This is Playwright using python in Page Object Model Pattern, please find all the documentation in this Readme file.

## Simple Description
This framework using minimalist POM pattern, but can be developed for further development. I'm using POM (Page Object Model) as the pattern in this framework, with structure:
- all of the page component are listed under pages folder with naming prefix of page_*.py
- all test are under testcases folder with naming prefix test_*.py
- all test data under test_data folder, to simplified test data usage
- all configs such as Broser Type, Headless Run, are under configs folder
- i encapsulate all precondition and setup on setup_test.py to simplified the testcase creation (WIP for util folder)
- test_suite.py is used to run group of testcases

Please find this structure
```
Store
|--> configs : global wide and config which used by the framework
|--> pages : all component which used by testcases
|--> test_data : all test data used by testcases
|--> testcases : all of testcases are stored here
|-> setup_test.py
|-> test_suite.py
```

### How To Run On Local

#### Run The Web App
1. Create venv by using
````
python3 -m venv test_env
````
2. Download Flask using pip
````
pip install flask
````
3. Activate the venv
```
source test_env/bin/activate
```
2. Run the app on a terminal
````
python3 app.py
````

#### Test the testcases
1. Create venv by using
````
python3 -m venv test_env
````
2. Activate the venv
```
source test_env/bin/activate
```
3. make sure playwright is installed by using 
```
pip install playwright
```
4. run the test suite to run all
```
python3 -m unittest -v test_suite.py
```

#### using allure integration
1. Download allure library
````
pip install allure-pytest
pip install allure-python-commons
````
2. Download allure report, using these tutorial https://allurereport.org/docs/install/
3. Run using allure
```
pytest test_suite.py --alluredir=./allure-results
```
4. Generate the allure report 
```
allure generate allure-results -o allure-report
allure open allure-report
```

## License

TBA