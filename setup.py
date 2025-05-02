from setuptools import setup, find_packages

setup(
    name="routine_generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "pandas",
        "reportlab",
    ],
    author="Joydeb Gan Prokas",
    description="A Streamlit app for generating academic routines",
    python_requires=">=3.7",
) 