import subprocess

import setuptools

try:
    import pypandoc

    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()


def get_tag():
    tag = subprocess.getoutput('git tag --sort=version:refname | tail -n1')
    commits = subprocess.getoutput(f'git rev-list {tag}..HEAD --count')
    return f'{tag}.{commits}'


setuptools.setup(
    name="finstruments",
    version=get_tag(),
    author="Kyle Loomis",
    author_email="kyle@spotlight.dev",
    description="Financial Instruments.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://kyleloomis.com/articles/financial-instrument-library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.7",
    packages=setuptools.find_packages(
        include=['spotlight*'],
        exclude=['tests.*']
    ),
    install_requires=[
        "pydash>=7.0.3",
        "pydantic==1.10.17",
        "pytz==2024.2",
        "workalendar==17.0.0"
    ]
)
