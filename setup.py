from distutils.core import setup
import setuptools

setup(
    name="seodo",
    version="0.0.14",
    packages=['seodo'],
    description="Seo.do terminal client",
    long_description=open('README.md', encoding="utf8").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/seodotdo/seodo-cli",
    author="Seo Do",
    author_email="cli@seo.do",
    maintainer="Seo Do",
    maintainer_email="cli@seo.do",
    keywords=['seo', 'keyword grouping', 'serp', 'keywords', 'search volume'],
    classifiers=[
        'Programming Language :: Python',
        'Environment :: MacOS X',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts':
            ['seodo=seodo.main:app']
    }

)