from setuptools import setup, find_packages

setup(
    name='Uni_Utils_Python',  # Nombre de tu paquete
    version='0.1.0',  # Versión de tu paquete
    author='Xavier Martin',  # Tu nombre
    author_email='martintapiaxavier@gmail.com',  # Tu correo electrónico
    description='Una biblioteca que contiene funciones, clases y demás que he ido creando a lo largo de mi curso universitario y me han resultado útiles.',
    long_description=open('README.md').read(),  # Lee el README para la descripción larga
    long_description_content_type='text/markdown',  # Tipo de contenido de la descripción larga
    url='https://github.com/tu_usuario/mi_biblioteca',  # URL del repositorio del paquete
    packages=find_packages(),  # Encuentra automáticamente todos los paquetes
    classifiers=[  # Clasificadores para ayudar a categorizar tu paquete
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Versión mínima de Python
)
