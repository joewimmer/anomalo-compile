from setuptools import setup, find_packages

setup(
    name='anomalo-compile',
    version='0.1.0',
    author='Joe Wimmer',
    author_email='joe@anomalo.com',
    description='A CLI tool to compile Jinja2 templates into YAML configurations for the Anomalo CLI tool.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/joewimmer/anomalo-compile',
    packages=find_packages(),
    install_requires=[
        'Jinja2>=2.11.0',  
        'PyYAML>=5.3',     
        'anomalo>=0.21.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'anomalo-compile=anomalo_compile.compiler:main',
        ],
    },
)
