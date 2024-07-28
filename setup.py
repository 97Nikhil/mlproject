from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
        This function will return the list of requirements
    '''
    requirmenets=[]
    with open(file_path) as file_obj:
        requirmenets=file_obj.readlines()
        requirmenets=[req.replace("\n","")for req in requirmenets]

        if HYPEN_E_DOT in requirmenets:
            requirmenets.remove(HYPEN_E_DOT)

    return requirmenets



setup(

    name='mlproject',
    version='0.0.1',
    author='Nikhil',
    author_email='nikhilchitoria1072003@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),


)