from setuptools import find_packages,setup

from typing import List


hyphen = '-e .'
def get_requirements(filepath:str)->List[str]:
    with open(filepath) as f:
        requirements = f.read().splitlines()
        if hyphen in requirements:  #as we have used -e . in our requirements.txt file to connect with our setup.py file, so we must remove them here
            requirements.remove(hyphen)
        return requirements  #returning the list of the required packages



setup(
    name='mlproject',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author='asok',
    author_email='ashoktmg205@gmail.com',
)

