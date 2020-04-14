import setuptools

with open("README.rst", "r") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="limecore-messaging-rabbitmq",
    version="0.1.0",

    description="limecore: Messaging (RabbitMQ)",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/limecore/messaging-rabbitmq",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    author="Daniel Bradberry",
    author_email="daniel@danielbradberry.com",
    
    license='MIT',
    
    package_dir={'': 'src'},
    packages=[
        'limecore.messaging.rabbitmq',],
    
    install_requires=required,
    python_requires='>=3.7',
)
