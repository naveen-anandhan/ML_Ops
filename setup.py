from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from a given file.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='end-to-end-deployment',   # Project Name
    version='0.0.1',  
    author='Naveen',
    author_email='naveen.ananadhan@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)
