from setuptools import setup, find_packages

setup(name="SIF-EC SDK",
      version="0.0.1",
      packages=find_packages(),
      install_requires=["apscheduler==3.11.0",
                        "fastapi[standard]==0.115.0",
                        "psutil==6.0.0",
                        "urllib3==2.2.2"
                        ],
      pyton_requires=">=3.12"
      )
