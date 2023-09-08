from setuptools import find_packages, setup

setup(
    name="flaskr",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "flask==2.3",
        # List your project dependencies here, e.g.
        # "numpy>=1.0",
        # "pandas>=1.0",
    ],
    entry_points={
        "console_scripts": [
            # If your project has command-line scripts, add their entry points here, e.g.  # noqa: E501
            # "my_script=my_package.my_module:main",
        ],
    },
    python_requires="==3.8",
    # Add metadata about your project
    author="aboudeh",
    author_email="aboudeh.link@gmail.com",
    description="The basic blog app built in the Flask tutorial.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/your_username/your_repository",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
