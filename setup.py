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

setuptools.setup(
    name="finstruments",
    use_scm_version=True,  # Enable setuptools_scm for versioning
    setup_requires=["setuptools_scm"],  # Ensure setuptools_scm is available for setup
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
        "python-dateutil==2.9.0.post0"
    ],
)
