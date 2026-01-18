from setuptools import setup, find_packages

setup(
    name='SmartPi',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy'
        # 'tflite-runtime'  # Uncomment on Raspberry Pi if you want TensorFlow Lite
    ],
    description='SmartPi AI: Offline ChatGPT-style chatbot for Raspberry Pi',
    author='ollie333333',
    author_email='your.email@example.com',
    entry_points={
        'console_scripts': [
            'smartpi-chat=smartpi.gui:run_gui'
        ]
    }
)
