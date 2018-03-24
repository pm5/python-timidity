
from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))

def readme():
    with open(os.path.join(here, "README.md")) as fh:
        return fh.read()


setup(name="timidity",
      version="0.1.0",
      description="A Python wrapper of Timidity++",
      long_description=readme(),
      classifiers=[
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 2.7",
          "Topic :: Multimedia :: Sound/Audio :: MIDI",
          "Topic :: Multimedia :: Sound/Audio :: Sound Synthesis",
      ],
      keywords="midi music player synthesizer",
      url="http://github.com/pm5/python-timidity",
      author="Pomin Wu",
      author_email="pomin5@gmail.com",
      license="MIT",
      packages=["timidity"],
      install_requires=[],
      include_package_data=True,
      dependency_links=[],
      test_suite="tests",
      tests_require=["nose"],
      zip_safe=False)
