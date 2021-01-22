import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="momentum",
    version="0.0.3",
    description="Time series models as pure functions, hyper-optimized by all the popular packages",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/momentum",
    author="microprediction",
    author_email="pcotton@intechinvestments.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["momentum"],
    test_suite='pytest',
    tests_require=['pytest','creme','scipy','numpy'],
    include_package_data=True,
    install_requires=["wheel","pathlib"],
    entry_points={
        "console_scripts": [
            "momentum=momentum.__main__:main",
        ]
    },
)
