import setuptools

setuptools.setup(
    name='hello-world',
    version='0.0.1',
    author="Adhita Selvaraj <adhita.selvaraj@gmail.com>",
    author_email='adhita.selvaraj@gmail.com',
    license="Apache License Version 2.0",
    description="Hello world app.",
    long_description="Hello World",
    url="https://github.com/swiftdiaries/codefest-build-system",
    packages={},
    package_data={},
    include_package_data=False,
    zip_safe=False,
    classifiers=(
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
    extras_require={
        'dev': [
            'pytest',
            'pytest-pep8',
            'pytest-cov'
        ]
    }
)
