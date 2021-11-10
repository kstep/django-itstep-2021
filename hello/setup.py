from setuptools import find_packages, setup

setup(
    name="django_itstep_2021",
    author_email="me@kstep.me",
    author="Konstantin Stepanov",
    description="Example Django project",
    url="https://github.com/kstep/django-itstep-2021",
    license='MIT',
    version='0.0.1',
    packages=find_packages(),
    scripts=['manage.py'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
    ],
)