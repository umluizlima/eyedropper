from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="eyedropper",
    version="0.0.2",
    author="Luiz Lima",
    author_email="umluizlima@gmail.com",
    license="MIT License",
    description="Easily get color codes on your computer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/umluizlima/eyedropper",
    py_modules=['eyedropper'],
    install_requires=['pyautogui', 'pyperclip'],
    entry_points={
        'console_scripts': [
            'eyedropper=eyedropper:run',
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
