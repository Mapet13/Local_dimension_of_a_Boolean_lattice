# Local dimension of a Boolean lattice
The repository contains tools, that were used to find local realizers of a Boolean lattice. 

More details will be provided in the upcoming paper of the same tile. 


## Repository structure
 - `data\`
    - `orders4.in` - Local realizer of $\mathcal{B}_4$ with a frequency of 3,
    - `orders7.in` - Local realizer of $\mathcal{B}_7$ with a frequency of 5,
 - `verify.py` - The script can be used to verify if local realizers from the data directory are correct,
 - `local_dim.ipnb` -  The Jupyter Notebook for generating SAT formulas, that find local, realizers for given properties. The notebook also parses SAT-solver output producing output as in `data` directory.


 ## Toolset
 - [The Kissat SAT Solver](https://github.com/arminbiere/kissat) (version: 4.0.2)
 - [SageMath](https://www.sagemath.org/) (version: 10.6)
 - [Python](https://www.python.org/) (version: 3.12.11)

## License
This code is licensed under the MIT license (see `LICENSE` file).
