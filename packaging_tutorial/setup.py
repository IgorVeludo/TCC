from setuptools import setup, find_packages

setuptools.setup(
    name="TCC", # Replace with your own username
    version="0.0.1",
    packages=find_packages(),
    include_package_data = True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        TCC=github_api.runner:start
    ''',

)
