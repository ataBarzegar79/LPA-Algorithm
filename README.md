## Label Propagation Algorithm 

This Algorithm provides a way to determine communities among a network\
for detailed information  take a look at  [this link](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.76.036106)

## Benefits
### Simple algorithm  : ###
It is very simple to understand and contains only  5 steps of operations . 

### Time efficiency :   ###
This algorithm is done in near linear time and it is a very big advantage . 

### No need for priory data : ###
One of the most interesting parts of this schema is that we need no additional data for  separating the communities . 

## Disadvantages ## 

###  Random  selection of Communities:  ###
In this algorithm and in 3 steps we are doing some works randomly , but one of them can cause wrong community sepration 
for us and finally the community detection will fail .  


## How does it work ? ## 

Simply we are reading network data from smple directory . 
you can add any file you want to use in algorithm to this
directory , but it should support the standard structure 
we have in project (take  look at karate_club.txt)


### Karate club data set ### 
As told above for this project we are using one data set ([karate club data set](http://konect.cc/networks/ucidata-zachary/))
at this project , but feel free to use others . 