# How to Use Chart.js with Django

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.0-brightgreen.svg)](https://djangoproject.com)

Code example used in the tutorial [How to Use Chart.js with Django](https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html).

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/sibtc/django-chartjs-example.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Load the data from fixtures:

```bash
python manage.py loaddata countries.json cities.json
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


## License

The source code is released under the [MIT License](https://github.com/sibtc/django-chartjs-example/blob/master/LICENSE).