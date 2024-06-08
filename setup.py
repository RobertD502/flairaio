import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flairaio",
    version="0.2.0",
    author="Robert Drinovac",
    author_email="unlisted@gmail.com",
    description="Asynchronous Python library for Flair's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/RobertD502/flairaio',
    keywords='flair, flair systems, flair api, flair api oauth2, flair client, flair vent, flair puck, flair bridge',
    packages=setuptools.find_packages(),
    python_requires= ">=3.7",
    install_requires=[
        "aiohttp>=3.8.1",
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ),
    project_urls={  # Optional
    'Bug Reports': 'https://github.com/RobertD502/flairaio/issues',
    'Source': 'https://github.com/RobertD502/flairaio/',
    },
)
