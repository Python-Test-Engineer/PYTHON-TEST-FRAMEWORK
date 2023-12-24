# Python Testing

<!-- <div>
   <img src="./_images/pytest.svg" width="75" height="75">
   <img src="./_images/playwright.png" width="75" height="75" >
   <img src="./_images/selenium.png" width="75" height="75" >
   <img src="./_images/pytest-flask.webp" width="75" height="75">
   <img src="./_images/pytest-django.jpg" width="75" height="75" >
   <img src="./_images/pytest-bdd.png" width="75" height="75" >
   <img src="./_images/py-behave.png" width="75" height="75" >
</div> -->

## PyTest - Playwright - Django - BDD - Hypothesis 

## A number of test suites with increasing elements of the above.

# Purpose

### In my training and work as a Python Test Engineer, I have come across a great many resources.

### I have collated them into fully integrated tests suites that have a straight forward set up and 150+ test templates, including mocking and patching.

### The test suites in this repo are all fully self contained and build on the previous suite along with a Django Test Suite.

# Python Testing Resources

- I collate a range of Python Testing resources from YT, Python Conferences and other sources, theerby providing a comprehensive resource for testers. Some resources are condensed for ease of use.

- Documentation and YT videos are included to enable ease of use. (Starting Dec 23)

# TEST_SUITE_00 status: v1.0.0

- This is a bare bones test suite with just the set up test code and tests to ensure all is working. 
- Download and set up venv and run `python -m pip install -r requirements_TEST_SUITE_01.txt`
- run `python -m pytest` and you will hae all tests displayed with pytest-sugar.


# TEST_SUITE_01 status: RC Alpha

## Installation

- git clone repo
- cd TEST_SUITE_01
- install instructions in README.md gut are:
- cd TEST_SUITE_01
- create virtual env (python -m venv venv then activate .\venv\Scripts\activate for Windows).
- `python -m pip install -r requirements_TEST_SUITE_01.txt`
- `python -m pytest` - this will ensure all paths are found if *pytest* itself does not work.

## About

- This is the foundation test suite that contains templates for PyTest and Playwright/Selenium. 
- The **src** folder is where devs place their code.
- The **tests** folder is where devs place their tests and contains templates.
- The **pytest.ini** folder is the first configuration file where test_suite options can be stored. Not used programatically in TEST_SUITE_01. **utils/myconfigparser.py** reads this file.
- Custom logger format etc in pytest.ini
- There are a number of test templates from various sources and include a wide range of PyTest features as well as a sectiion on MOCKING, (05_mocks).
- Acknowledgements and links to YT videos and other resources are cited.

# TEST_SUITE_02 status: RC Beta

- all of TEST_SUITE_01 plus Playwright and API testing.

# TEST_SUITE_03 status: NOT INCLUDED JUST YET

- all of TEST_SUITE_02 plus BDD.

# TEST_SUITE_HYPOTHESIS status: WIP

- all of TEST_SUITE_03 with the addition of property based testing.

# TEST_SUITE_DJANGO: status: Alpha

### A simple Django site with unittest, pytest-django and e2e Playwright testing.
