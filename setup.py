from setuptools import setup, find_packages


setup(
    name="opening hours parsing",
    version='0.0.2',
    description="Parse opening hours",
    author="Mohammed Salman",
    author_email="m.salman@zinkki.com",
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=["parsing_tools"],
    setup_requires=['pytest-runner', 'mock'],
    tests_require=['pytest', 'mock'],
    url='https://github.com/muhis/opening_hours_lib'
)
