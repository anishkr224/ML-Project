# with the help pf setup.py i will be able to build my entire ML application as package and even deploy in PyPI and from there anybody can do installation and anybody can also use it

from setuptools import find_packages,setup  # automatically find out all the packages that are available in the entire ML application, the directory thet we have created
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements] # replace \n with blank in 'requirements.txt'

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
name='mlproject',
version='0.0.1',
author='Anish',
author_email='anishkumar3967@gmail.com',
packages=find_packages(),
# install_requires=['pandas','numpy','seaborn']
install_requires=get_requirements('requirements.txt')

)