from setuptools import setup
from pathlib import Path

directory = Path(__file__).resolve().parent
with open(directory / 'README.md', encoding='utf-8') as f:
  long_description = f.read()

setup(name='aht',
      version='0.1',
      packages = ['aht', 'aht.core.io', 'aht.core.logging'],
      long_description=long_description,
      long_description_content_type='text/markdown',
      )