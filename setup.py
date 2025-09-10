from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cto-agent",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="An AI-powered Chief Technology Officer agent for strategic technology leadership",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cto-agent",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Office/Business",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        # Add your package dependencies here
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.12b0",
            "isort>=5.10.1",
            "mypy>=0.931",
            "pylint>=2.12.2",
        ],
    },
)
