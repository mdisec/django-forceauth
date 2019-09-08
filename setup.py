import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-forceauth',  
    version='0.1',
    author="Mehmet D. INCE",
    author_email="mehmet@mehmetince.net",
    license="GPLv3",
    description="A Django package that force authentication requirement by default on every single endpoint.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/javatechy/dokr",
    #packages=setuptools.find_packages('forceauth'),
    packages=['forceauth'],
    keywords=["django", "authentication", "securedesign"],
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
 )