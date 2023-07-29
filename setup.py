from setuptools import setup, find_packages

setup(
    name='daily-task-manager',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'tabulate'
    ],
    entry_points={
        'console_scripts': [
            'daily_task_manager = daily_task_manager.script:main'
        ]
    },
)
