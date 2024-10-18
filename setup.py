import subprocess

import setuptools

try:
    import pypandoc

    try:
        long_description = pypandoc.convert_file('README.md', 'rst')
    except Exception as e:
        print(f"Warning: pypandoc failed with {e}, falling back to raw README.md")
        with open('README.md', encoding='utf-8') as f:
            long_description = f.read()
except ImportError:
    print("Warning: pypandoc not found, using raw README.md")
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()


def get_tag():
    try:
        tag = subprocess.run(
            ['git', 'tag', '--sort=version:refname'],
            check=True,
            text=True,
            capture_output=True
        ).stdout.strip().split('\n')[-1]

        commits = subprocess.run(
            ['git', 'rev-list', f'{tag}..HEAD', '--count'],
            check=True,
            text=True,
            capture_output=True
        ).stdout.strip()

        return f'{tag}.{commits}'
    except subprocess.CalledProcessError:
        print("Warning: Unable to determine version from Git, using default version 0.0.0")
        return '0.0.0'


version = get_tag()

setuptools.setup(
    name="finstruments",
    version=version,
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
        include=['finstruments*'],
        exclude=['tests.*']
    ),
    install_requires=[
        "pydash>=7.0.3",
        "pydantic==1.10.17",
        "pytz==2024.2",
        "workalendar==17.0.0"
    ]
)
