import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt','r') as fr:
    requires = fr.read().split('\n')

setuptools.setup(
    # pip3 install test-lib
    name="DevEviI", # Replace with your own username
    version="0.2.1",
    author="XF",
    author_email="x6uc88@gmail.com",
    description="bY ~ t.me/DevEviI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wqfa/DevEviO",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=requires,
)
