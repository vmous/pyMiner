try:
    from setuptool import setup
except ImportError:
    from distutils.core import setup

config = {
    'name' : 'pyMiner',
    'version' : '0.1',
    'description' : 'Python implementations of various data mining and machine learning algorithms.',
    'author' : 'Vassilis S. Moustakas',
    'author_email' : 'vsmoustakas@gmail.com',
    'license' : 'Apache v.2.0',
    'url' : 'https://github.com/vmous/pyMiner',
    'packages' : ['miner']
}

setup(**config)
