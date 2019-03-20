import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='afautils',  

     version='0.1',

     scripts=['afautils'] ,

     author="flyingpeter",

     author_email="pmandrade@academiafa.edu.pt",

     description="Latin chars replacement",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/flyingpeter/repository/blob/master/README.md",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "Operating System :: OS Independent",

     ],

 )
