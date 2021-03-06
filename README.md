# Spatial search by quantum walk
## File naming convention
The Hamiltonian and Kets classes are located in the `qualk/quantum` module, 
named `hamiltonian.py` and `ket.py` respectively. It is not necessary to change these. 
They have not been documented yet, however, they are reasonably self-explanatory.

The file `main.py` contains imports the functions that could be run. 

The plotting modules begin with the prefix `p + *number*`. They can be run by 
simply setting using the run function in the module:
```
p2_marked_state_probability_against_time.run()
```

`plots.py` contains the plotting functions used by the scripts. The plots are 
saved to the `/plots` subdirectory named for the prefix of the plot-generating 
script that produced it.

## Make a new plot
Change the parameters for a specific plot in `qualk/config.py`. The global variables 
`alpha`, `dimensions`, and `marked_state` are defined at the top of the script. 
Additional parameters for the specific plotting scripts can be changed in the 
parameters dictionaries that are prefixed by the corresponding plot number. 

Then just run the plots defined in `main.py`:
```
python main.py
```
