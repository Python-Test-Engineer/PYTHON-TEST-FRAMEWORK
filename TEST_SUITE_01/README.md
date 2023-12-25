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
- The **pytest.ini** folder is the first configuration file where test_suite options can be stored. Not used programatically in TEST_SUITE_01. **utils/myconfigparser.py** reads this file.
- Custom logger format etc in pytest.ini
- There are a number of test templates from various sources and include a wide range of PyTest features as well as a sectiion on MOCKING, (05_mocks_patch).
- Acknowledgements and links to YT videos and other resources are cited.

## Installation

- git clone repo
- cd TEST_SUITE_01
- install instructions in README.md gut are:
- cd TEST_SUITE_01
- create virtual env (python -m venv venv then activate .\venv\Scripts\activate for Windows).
- `python -m pip install -r requirements_TEST_SUITE_01.txt`
- `python -m pytest` - this will ensure all paths are found if *pytest* itself does not work.

