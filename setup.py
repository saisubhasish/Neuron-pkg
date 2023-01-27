import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()    #  From README.md

PKG_NAME = "Neuron_pkg"
USER_NAME = "saisubahsish"
PROJECT_NAME = "Neuron-pkg"

setuptools.setup(
    name=f"{PKG_NAME}-{USER_NAME}",
    version="0.0.3",
    author=USER_NAME,
    author_email="saisubhasishrout777@gmail.com",
    description="A small package for perceptron",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),   # find_packages() searches __init__py file and convert them to library
    python_requires=">=3.8",
    install_requires=[
        "numpy==1.23.0",
        "pandas==1.4.0",
        "joblib==1.1.0"
    ]
)