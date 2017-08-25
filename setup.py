from setuptools import setup

setup(
    name='opentsdb_rest_client',
    version='0.1',
    description='Python client for the OpenTSDB HTTP REST API',
    url='http://github.com/xblitz/opentsdb_rest_client',
    keywords=["opentsdb", "api", "client"],
    author='Eric Rouleau',
    author_email='xblitz@gmail.com',
    license='MIT',
    packages=['opentsdb_rest_client'],
    install_requires=[
        "requests >= 2.0.0",
    ],
    zip_safe=False
)
