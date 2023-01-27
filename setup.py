from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name='cobalt-cli',
    version='0.0.1',
    author='Mark Guthrie',
    author_email='m@rkguthrie.com',
    license='GNU 3.0',
    description='Command Line Interface for the Cobalt Application',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mgu3/cobalt_cli',
    py_modules=['cobalt-cli', 'app'],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],

    entry_points={
        'console_scripts': [
            'cobalt-cli = cobalt_cli:cli',
        ]
    }
)
