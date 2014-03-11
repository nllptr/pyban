from distutils.core import setup

setup(
    name='PyBan',
    version='0.2.0',
    author='Simon Wessel',
    author_email='simon.w.karlsson@gmail.com',
    packages=['pyban', 'pyban.test'],
    scripts=['bin/pyban-cli.py'],
    url='http://pypi.python.org/pypi/PyBan',
    license=TOBEDECIDED,
    description='Kanban with Python!',
    long_description=open('README.txt').read(),
    install_requires=[]
)
