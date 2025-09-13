from setuptools import setup
import json


with open('metadata.json', encoding='utf-8') as fp:
    metadata = json.load(fp)


setup(
    name='cldfbench_tarble1984nuevos',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['cldfbench_tarble1984nuevos'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'tarble1984nuevos=cldfbench_tarble1984nuevos:Dataset',
        ]
    },
    install_requires=[
        'pyglottography',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
