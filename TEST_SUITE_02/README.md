# generic python testing framework.

## PyTest - Playwright - Selenium - PytestBDD - Behave

## THREE test suites with increasing elements of the above.

<div>
   <img src="./_images/pytest.svg" width="75" height="75">
   <img src="./_images/playwright.png" width="75" height="75" >
</div>

# TEST_SUITE_01

- This is the foundation test suite that contains templates for PyTest and Playwright. 
- The **src** folder is where devs place their code.
- The **tests** folder is where devs place their tests and contains templates.
- The **pytest.ini** folder is the first configuration file where test_suite options can be stored. Not used in TEST_SUITE_01. **utils/myconfigparser.py** reads this file.

## To set up

- cd TEST_SUITE_01
- create virtual env (python -m venv venv then activate .\venv\Scripts\activate for Windows)
- pip install -r requirements_TEST_SUITE_01.txt
- dont forget *playwright install* as this loads browsers etc for Playwright
- *python -m pytest* - this will ensure all paths are found if *pytest* itself does not work.
- *python -m pytest .\tests\04_playwright\ --headed* to see browsers for playwright and you can usee the --headed when running all tests. Playwright default is headless.

