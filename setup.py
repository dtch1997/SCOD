"""setup.py for hessian_eigenthings"""

from setuptools import setup, find_packages

install_requires = [
    'numpy>=1.18.0',
    'torch>=1.7',
    'torchvision>=0.7.0',
    'torch-dct>=0.1.5',
    'tensorboard>=2.4.1',
    'tqdm>=4.15.0',
    'scipy>=1.4.1',
    'matplotlib>=3.1.3',
    'pandas>=1.0.1',
    'scikit-learn>=0.23.2',
    'seaborn>=0.11.1',
]

setup(name="nn_ood",
      author="Apoorva Sharma",
      install_requires=install_requires,
      packages=find_packages(),
      description='Equip arbitrary pytorch models with OOD detection',
      version='0.1.0')
