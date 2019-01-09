import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='leap_mouse',
        version='0.0.1',
        packages=setuptools.find_packages(),
        entry_points={
            'console_scripts':[
                'leap_mouse = leap_mouse.main:main',
            ],
        },
    )