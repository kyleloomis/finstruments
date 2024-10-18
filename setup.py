import subprocess

import setuptools

try:
    import pypandoc

    try:
        long_description = pypandoc.convert_file("README.md", "rst")
    except Exception as e:
        print(f"Warning: pypandoc failed with {e}, falling back to raw README.md")
        with open("README.md", encoding="utf-8") as f:
            long_description = f.read()
except ImportError:
    print("Warning: pypandoc not found, using raw README.md")
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read()


def get_tag():
    try:
        # TODO
        # # Attempt to get the latest tag
        # tag = subprocess.run(
        #     ["git", "describe", "--tags", "--abbrev=0"],
        #     check=True,
        #     text=True,
        #     capture_output=True,
        # ).stdout.strip()
        #
        # # Remove the 'v' prefix if it exists
        # if tag.startswith("v"):
        #     tag = tag[1:]
        #
        # # Verify that the tag is in a valid format
        # if not tag or not tag[0].isdigit():
        #     raise ValueError(f"Invalid tag format: {tag}")

        tag = "master"

        # Count the number of commits since the last tag
        commits_since_tag = subprocess.run(
            ["git", "rev-list", f"{tag}..HEAD", "--count"],
            check=True,
            text=True,
            capture_output=True,
        ).stdout.strip()

        # Form the new version
        # base_version = tag
        base_version = "0.1"
        new_version = f"{base_version}.{commits_since_tag}"

        return new_version
    except subprocess.CalledProcessError as e:
        # Handle the case where no tags are found
        if "fatal: No names found" in str(e):
            print("No tags found in the repository, using default version 0.0.1")
            return "0.0.1"
        print(f"Warning: Unable to determine version from Git: {e}")
        return "0.0.1"


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
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    packages=setuptools.find_packages(include=["finstruments*"], exclude=["tests.*"]),
    install_requires=[
        "pydash>=7.0.3",
        "pydantic==1.10.17",
        "pytz==2024.2",
        "workalendar==17.0.0",
    ],
)
