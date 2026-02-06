from setuptools import setup, find_packages

setup(
    name="aaayafuj",
    version="7.0.4",
    packages=find_packages(include=['aaayafuj', 'aaayafuj.*']),
    include_package_data=True,
    install_requires=[
        'cryptography>=41.0.0',
        'pyyaml>=6.0.1',
        'requests>=2.31.0',
    ],
    entry_points={
        'console_scripts': [
            'aaayafuj=aaayafuj.cli:main',
        ],
    },
    python_requires='>=3.8',
    author="Aaayafuj Cybersecurity",
    description="A modular, high-performance Python CLI toolset for security auditing.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/aaayafuj51-AYFJ/Aaayafuja_CyberSecurity7.py",
)