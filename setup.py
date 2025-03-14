from setuptools import setup, find_packages

setup(
    name="tearecomandation",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask>=2.0.1",
        "scikit-learn>=1.0.2",
        "pandas>=1.3.3",
        "numpy>=1.21.2",
        "joblib>=1.1.0",
        "Flask-WTF>=0.15.1",
        "Werkzeug>=2.0.1",
        "python-dotenv>=0.19.0",
    ],
    python_requires=">=3.8",
    author="Your Name",
    author_email="your.email@example.com",
    description="个性化茶饮推荐系统",
    keywords="tea, recommendation, chinese medicine",
    url="https://github.com/yourusername/tearecomandation",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
) 