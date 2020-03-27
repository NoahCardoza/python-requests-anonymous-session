import python_requests_anonymous_session
from setuptools import setup, find_packages


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


with open('README.md') as f:
    long_description = f.read()

setup(
    name="python-requests-anonymous-session",
    version=python_requests_anonymous_session.__version__,
    author="Noah Cardoza",
    author_email="noahcardoza@gmail.com",
    description="Randomizes the user agent, along with default headers found with that browser as well as the cipher suite used.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/NoahCardoza/python-requests-anonymous-session",
    install_requires=parse_requirements('requirements.txt'),
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
