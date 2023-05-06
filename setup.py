

from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name="generate-readme",
    version="0.1",
    description="Generate a README.md file for your projects",
    author="Adetunji Adetayo",
    author_email="<litcoderr@gmail.com>",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Navlos/Generate_Readme_cli.git",
    py_modules=["generate_readme"],
    keywords=["README", "python"],
    install_requires=["markdown"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",

        "License :: OSI Approved :: MIT License",



    ],

)
