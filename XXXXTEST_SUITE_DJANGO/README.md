# Django Testing

## REFERENCES

- ### Pybites - https://www.youtube.com/watch?v=L5jWFU2sVXQ
- ### Ssali Jonathan ites - https://www.youtube.com/watch?v=Nn3Yjea5KCI&list=PLEt8Tae2spYlVZUBBEE9PtX-NXk_hw7o4


## TODO

- ### DjangoStars - https://djangostars.com/blog/django-pytest-testing/

- ### https://pytest-with-eric.com/pytest-advanced/pytest-django-restapi-testing/#Conftest-and-Setup

- ### https://dev.to/sherlockcodes/pytest-with-django-rest-framework-from-zero-to-hero-8c4

- ### https://klementomeri.medium.com/path-to-tight-sleep-with-test-automation-81916b567745

### SETUP

- ### cd TEST_SUITE_DJANGO
- ### creater virtual env python -m venv venv
- ### pip install -r requirents.txt
- ### run *playwright install* to load in playwright browsers
- ### in one terminal run python manage.py runserver
- ### For unittests run `python manage.py test`
- ### in another run `python -m pytest -v` or `python -m pytest -v --headed` if using  playwright and you want to see browsers. Sometimes this may not work so you will need to add the headless=False to the test.
- ### DB has had migrations. superuser: admin password
- ### authuser uses a Custom User model so that login defaults to email and password. This can be removed so that the User model is used.
- ### pytest-sugar added for fancier terminal output
- ### PyBoxen used for fancy console output. Examples are in the orm app.
- ### django-extensions used in orm app so that we can run scripts in a py file rather than in shell. See `orm/_NOTES.md`

### Tests

- ### Based on Ssali's Django TDD, all his unittests are included and are in the tests.py of each app. The TDD video series establish a great many tests for us to use.
- ### I have also set up a tests folder for PyTest and converted Ssali's tests into PyTest versions along with samples from the other references.
- ### You can also get PyTest to run unittests in dDjango apps `python -m pytest .\ ` where .\ is the root of the project or you can use ` python -m pytest -vs .\posts` for a particular app. 


