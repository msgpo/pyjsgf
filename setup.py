from setuptools import setup


def get_long_description():
    with open('README.rst') as f:
        return f.read()


setup(
    name='pyjsgf',
    description='JSpeech Grammar Format (JSGF) compiler, matcher and parser '
                'package for Python.',
    long_description=get_long_description(),
    url='https://github.com/Danesprite/pyjsgf',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'Topic :: Software Development :: Libraries',
    ],
    author='Dane Finlay',
    author_email='Danesprite@gmail.com',
    version='1.6.0',
    packages=['jsgf', 'jsgf.ext'],
    install_requires=['pyparsing', 'six']
)
