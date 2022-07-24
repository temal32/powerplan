import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="powerplan",
    version="0.0.2",
    author="Temal",
    author_email="contact@temal.cf",
    description="Get windows power plan name or guid and change power plan to any plan.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/temal32/powerplan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.0',
)