from distutils.core import setup

setup(
    name='PyBan',
    version='0.3.0',
    author='Simon Wessel',
    author_email='simon.w.karlsson@gmail.com',
    packages=['pyban', 'pyban.test'],
    url='https://github.com/multi8it/pyban',
    license='LICENSE.txt',
    description='Kanban with Python!',
    long_description=open('README.txt').read(),
    install_requires=[]
)
