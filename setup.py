from setuptools import find_packages,setup 
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    with open(file_path,'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
  
setup(
name='mlproject',
version='0.1',
author='nwenwe',
author_email='nnhwin16@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),


)