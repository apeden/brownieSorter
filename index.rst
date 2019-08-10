.. brownieSort documentation master file, created by
   sphinx-quickstart on Sun Jul 28 20:03:27 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to brownieSort's documentation!
=======================================
This is a project to create a module that sorts
people (in this case brownies) into groups
according to friendships as declared in a 
text (.txt0) file. Brownies names followed
by a comma and then comma separated names of the 
friends of the said brownie are entered into
the text file: e.g::
	Anna, Julie, Samantha
	Julie, Anna, Chloe, Jill
	Brioney, Claudia, Jennifer, Debs
	Debs
In the above, Anna has declared two friends: Julie and Samantha.
Julie has declared three, including the above named Anna.
Debs has not declared any friends. In the text file, it is 
not permissible for a friend to be mentioned, who is not also
the first name of a line somewhere in the file. 

Based on the friendship, the code sorts the friends into
n groups of equal (or nearly equal) size. The aim is to 
achieve the happiest combinations of groups.

.. automodule:: camp
    :members:

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   all-about-me



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
