# Advanced Networked Systems SS25

This repository contains code skeleton for the labs of Advanced Networked Systems SS25 at Paderborn University, Germany. There are in total three labs, which will be released one by one throughout the semester. For more details, please refer to the lab descriptions released on PANDA.

# Tom: Additional Requirements 
ryu needs pip==20.3.4 (https://github.com/faucetsdn/ryu/blob/master/pip-requirements.txt). 
- Therefore **downgrade** pip before continuing

##### NOTES
https://mininet.org/download/#option-3-installation-from-packages


##### TEST
go into ryu folder. Then execute this:
``ryu run --observe-links ryu/app/gui_topology/gui_topology.py``

In another terminal, execute this:
``sudo mn --controller remote --topo tree,depth=3``

When finished, execute this:
``mn -c``