from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    as per the file path provided.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    
    if '-e .' in requirements:
        requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(    
    name='firstDS',
    version="0.0.1",
    author= "Ali kumbhar",
    author_email= "sherry@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt') 
    # this function read all package we have saved in the requirements.txt
    #install_requires = ['pandas', 'numpy'],
    
    )
    