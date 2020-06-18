from setuptools import setup

url = ""
version = "0.1.0"
readme = open('README.rst').read()

setup(
    name="icon_prometheus_exporter",
    packages=["icon_prometheus_exporter"],
    version=version,
    description="Package to do something useful",
    long_description=readme,
    include_package_data=True,
    author="Haitham Ghalwash",
    author_email="h.ghalwash@gmail.com",
    url=url,
    install_requires=[],
    download_url="{}/tarball/{}".format(url, version),
    license="MIT"
)
