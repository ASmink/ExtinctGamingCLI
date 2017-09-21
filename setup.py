from setuptools import setup

setup(
    name='extinct-gaming-cli',
    version='0.1',
    py_modules=['extinct'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        extinct=extinct:cli
    ''',
)
