import pathlib

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


# This call to setup() does all the work
setup(
    name="django-django_bootstrap",
    zip_safe=False,
    version="2.3.2",
    description="Bootstrap 4 for Django",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/zostera/django-bootstrap",
    author="Dylan Verheul",
    author_email="dylan@dyve.net",
    license="BSD-3-Clause",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    install_requires=[
        "Django>=2.2",
        "beautifulsoup4>=4.8.0",
        'importlib-metadata<3; python_version<"3.8"',
    ],
)
