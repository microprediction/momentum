# momentum ![tests](https://github.com/microprediction/momentum/workflows/tests/badge.svg) ![deploy](https://github.com/microprediction/momentum/workflows/deploy/badge.svg)
A mini-package for computing the running mean, variance, kurtosis and skew

- No dependencies ... not even numpy.
- No classes ... unless you want them.
- State is a dict, for trivial serialization. 
- Tested against scipy, creme, statistics

### Install 

    %pip install momentum

### Usage: running mean, var

    from momentum import var_init, var_update
    from pprint import pprint
    
    m = var_init()
    for x in [5,3,2.4,1.0,5.0]:
        m = var_update(m,x)
    pprint(m)
    
    

### Usage: running mean, var, kurtosis and skew 

    from momentum import kurtosis_init, kurtosis_update
    
    m = kurtosis_init()
    for x in [5,3,2.4,1.0,5.0]:
        m = kurtosis_update(m,x)
    pprint(m)
    
    
File an issue if you need more help using this. 
    
  
### Usage: running recency-weighted mean, var

    from momentum import forgettingvar_init, forgettingvar_update
    from pprint import pprint
    
    m = rvar_init(rho=0.01,n=15)
    for x in [5,3,2.4,1.0,5.0]:
        m = rvar_update(m,x)
    pprint(m)
    
This will switch from running variance to a weighted variance after 15 data points. 
    