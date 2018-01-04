This is a dataset about breast cancer occurences. Breast cancer is the most commonly 
diagnosed cancer in women and is the second leading cause of cancer death among women.

## Data

This dataset is taken from [OpenML - breast-cancer](https://www.openml.org/d/13)

This breast cancer domain was obtained from the University Medical Centre, Institute of Oncology, Ljubljana, Yugoslavia. Thanks go to M. Zwitter and M. Soklic for providing the data. 
Please include this citation if you plan to use this database.

Matjaz Zwitter & Milan Soklic (physicians) Institute of Oncology University Medical Center Ljubljana, Yugoslavia -- Donors: Ming Tan and Jeff Schlimmer (Jeffrey.Schlimmer@a.gp.cs.cmu.edu) -- Date: 11 July 1988.

* 286 instances
* 10 attributes
* Missing values: yes

Class Distribution:
* no-recurrence-events: 201 instances
* recurrence-events: 85 instances

Data is located in directory `data`

`data/breast-cancer.csv`

## Preparation

To get our output data several things are done to input data:
* missing values marked with "?" are replaced with ""(empty space)
* all " are removed
* all ' are removed
* yes and no values are replaced with true and false

Scripts for dataset are located in directory `scripts`

`scripts/main.py`

## License
Licensed under the [Public Domain Dedication and License][pddl] (assuming
either no rights or public domain license in source data).

[pddl]: http://opendatacommons.org/licenses/pddl/1.0/