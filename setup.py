from setuptools import setup, find_packages

setup(
    name='wf_console',
    version='0.0.11',
    packages=find_packages(),
    install_requires=['pandas'],
    description='My custom console class.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Weston Forbes',
    url='https://github.com/westonforbes/wf_console.git',
    python_requires='>=3.11.2',
)