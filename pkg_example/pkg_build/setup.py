# Execute a command below to build package
# python setup.py bdist_wheel
# When you install custom package, pip install ./mypkg.whl
import setuptools



setuptools.setup(
    name="mypkg_name", # Replace with your own username
    version="1.0.0",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)