from setuptools import setup

setup(
    name='lrc_dl',
    version='0.1.0',
    description='An ultimate cli tool for downloading song lyrics, inspired by other awesome *-dl programs.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=[
        "lrc_dl",
        "lrc_dl.providers",
    ],
    entry_points={
        'console_scripts': ['lrc-dl=lrc_dl.main:main'],
    },
    install_requires=[
        "httpx>=0.24.1",
        "beautifulsoup4>=4.13.3",
        "mutagen>=1.46.0",
        "yt-dlp>=2023.10.13",
    ]
)
