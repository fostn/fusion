from setuptools import setup,find_packages
setup(
    name="fusion",
    version="1.0",
    py_modules=["Fusion"],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fusion = Fusion:Fusion"
        ]
    },
    install_requires=[
        "requests","blessed","pexpect"
    ],
)
