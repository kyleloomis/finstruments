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
        # Get the latest tag
        tag = subprocess.run(
            ['git', 'describe', '--tags', '--abbrev=0'],
            check=True,
            text=True,
            capture_output=True
        ).stdout.strip()

        # Make sure the tag starts with a valid semantic version format (e.g., v1.0.0)
        if tag.startswith('v'):
            tag = tag[1:]

        # Verify the tag follows semantic versioning
        if not tag or not tag[0].isdigit():
            raise ValueError(f"Invalid tag format: {tag}")

        # Count the number of commits since the last tag to append
        commits_since_tag = subprocess.run(
            ['git', 'rev-list', f'{tag}..HEAD', '--count'],
            check=True,
            text=True,
            capture_output=True
        ).stdout.strip()

        # If there are no commits, use the tag as the version
        if commits_since_tag == '0':
            return tag

        # Return the tag with the number of commits appended
        return f"{tag}.{commits_since_tag}"
    except (subprocess.CalledProcessError, ValueError) as e:
        print(f"Warning: Unable to determine version from Git: {e}")
        return '0.1.0'  # Default to a safe version if there's a problem


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
