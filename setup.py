from setuptools import setup, find_packages

dependencies = [
    "typer>=0.6", 
    "structlog>=22.1.0",
    "matplotlib>=3.6.2",
    "numpy>=1.23.5"
    ]
dev_dependencies = [
    "pytest>=7.1",
    "flake8>=5",
]

setup(
    name="arrayopt",
    description="Scripts to find optimal array locations",
    version="0.2",
    install_requires=dependencies,
    extras_require={
        "dev": dev_dependencies,
    },
    # entry_points={
    #     "console_scripts": [
    #         "converter = roman.cli:main"
    #     ]
    # },
    packages=find_packages("src"),
    package_dir={"": "src"},
)