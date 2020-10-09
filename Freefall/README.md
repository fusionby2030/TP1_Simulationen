# Freefall Simulation Code 

### Freefall2.py

The file *freefall2.py* provides the positions and velocities of **n** particles with equal mass and equal size (variable **radius**) for elastic collisions. 

It is broken up into 2 classes, which have variable parameters as described below. 

##### Class Particle

- r, v
    - position and velocity vectors (numpy arrays)
- radius
    - size of particle (float)
- lattice
    - if the particle has not been hit yet, it is still 'connected' to a lattice and does not move, see *advance* function (boolean)

##### Class Simulation 
- n 
    - number of particles (integer)
- particles 
    - list of particle objects that is created through the *init_particles* function (list)
    
The simulate function calls *draw_graph* at the end to produce a graph over time of the positions and velocities. 
One can simply remove the call to *draw_graph* and instead return the position lists. 


### Freefall1.py 
Similarly the file *freefall1.py* simulates freefall, but this time for the inelastic case.
One needs to add a return statement just like *freefall2.py* to recieve the positions and velocities at the end. 

 