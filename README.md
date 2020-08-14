# HSlib

This library is intended to be used to help heathstone players not have their brains hurt when calculating stupid math stuff while playing.
if you would like your brain to hurt less while playing a certian deck where particular problems arises, feel free to add that item into the issues tab.

running HSlib

1)  open up your local terminal with python installed
2)  navigate to the HS lib folder, 
3)  open the python interpreter,
4)  use ">import HSlib as *" (this command will allow our methods to be called as just their name, if you would prefer to add HSlib. before method calls, use ">import HSlib")
5)  use the methods included

Learning the methods

1)  do steps 1-3 of "running HSlib"
2)  use "
    >import HSlib"
3)  use 
'''python

    >for meth in filter(lambda x: x not in HSlib.selfignore, dir(HSlib)):
    >    help("HSlib." + meth)
    >
''''
\4) see the documentation for each method in the library


Learning a method

1)  do steps 1-4 of "running HSlib"
2)  use ">help('method')"  where 'method' is the name of the method you want to know about. 
