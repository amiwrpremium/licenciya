from distutils.core import setup

setup(
    name='licenciya',
    packages=['licenciya'],
    version='0.0.1',
    license='MIT',
    description='Licensing Library',
    author='amiwrpremium',
    author_email='amiwrpremium@gmail.com',
    url='https://github.com/amiwrpremium/licenciya/',
    download_url='https://github.com/amiwrpremium/licenciya/releases/tag/v_0.0.1',
    keywords=['License', 'Protection'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    package_dir={'': 'src'},
)
