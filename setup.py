from distutils.core import setup

setup(name='dojo_tdd',
      version='0.1',
      description='arquivos base para dojo tdd em python',
      author='Fábio Correia',
      author_email='fabio.correia@accenture.com',
      packages=['distutils', 'distutils.command'],
      py_modules=['dojo_tdd.main', 'tests.main_test'],
      )
