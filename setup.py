import setuptools

setuptools.setup(
    name="eol-custom-reg-form",
    version="0.0.1",
    author="constanzaaltamirano",
    author_email="constanzaaltamirano@uchile.cl",
    description="Eol custom reg form",
    long_description="Eol custom reg form",
    url="https://cajalosandes.virtual-labx.cl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "lms.djangoapp": [
            "eol_custom_reg_form = custom_reg_form.apps:EolCustomRegFormConfig",
        ]
    },
)
