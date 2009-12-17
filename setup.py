import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
setup(
    name = "sprang",
    version = "0.1",
    packages = find_packages(),
    author = "JingleManSweep",
    author_email = "jinglemansweep@gmail.com",
    description = "Helper shell script allowing posting and retrieving of text snippets via 'sprunge.us' pastebin service.",
    url = "http://code.google.com/p/django-testmaker/",
    include_package_data = True
)
