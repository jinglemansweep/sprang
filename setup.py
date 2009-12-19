#import ez_setup, os
#ez_setup.use_setuptools()
import os
from setuptools import setup, find_packages
setup(
    name = "sprang",
    version = "0.16",
    author = "JingleManSweep",
    author_email = "jinglemansweep@gmail.com",
    description = "Helper shell script allowing posting and retrieving of text snippets via 'sprunge.us' pastebin service.",
    url = "http://github.com/jingleman/sprang",
    packages = find_packages(),
    scripts = [os.path.join("bin", "sprang"),],
    include_package_data = True
)
