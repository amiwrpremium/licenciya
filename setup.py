from distutils.core import setup

setup(
    name='licensiha',
    packages=['licensiha'],
    version='0.0.1',
    license='MIT',
    description='Licensing Library',
    author='amiwrpremium',
    author_email='amiwrpremium@gmail.com',
    url='https://github.com/amiwrpremium/licensiha/',
    download_url='https://github.com/amiwrpremium/licensiha/archive/refs/tags/v_0.0.1.tar.gz',
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
)
