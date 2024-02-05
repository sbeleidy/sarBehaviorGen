# Assitive Behavior Generator for Social Robots

This package provides the interface for generating and executing  assistive behaviors of social robots.  The behaviors are intended to communicate a given *intent* while also attempting to meet various social norms and conventions for turn-taking, rapport development, and supporting user autonomy.

The behavior generation uses an ontology of social behaviors and a planner.  The ontology is realized in a hierarchical task network (HTN) model, and the planner (PyShop) uses this model to find a sequence of actions for the robot to perform.

The current HTN model can be found in models/misty.hddl.  This model describes behaviors for assisting a user on assembling a tangram puzzle.

The planner is PyShop, a derivative of Pyhop, both of which use the SHOP algorithm.  Unlike Pyhop, PyShop uses a declarative representation of the model, encoded in a hddl file.
You can download PyShop at https://github.com/FandM-CARES/pyshop.  You will need to install it to use the behavior generator.

This package also provides middleware to run the behaviors on social robots.  Currently, there are two supported platforms: the NAO and Misty robots.
The Misty interface also requires a Skill running on the robot.  You can find the code for that Skill at https://github.com/FandM-CARES/psiMisty.
The NAO interfaces uses a local server to receive the behavior and then execute it on the robot.  That code can be found at
https://github.com/SturgeonInc/nao_api.

## Executing

You can begin to test the behavior generator once you have installed PyShop.
Then you can quickly test it by running the following command:
```
python3 behavior_gen.py
```
This will use the default robot interface, which simply prints each action in the behavior to the terminal.

### NAO

To test the interface to a NAO robot, try the following:
```
python3 behavior_gen.py --nao --address 192.168.1.3
```
Replace the IP address for the NAO robot.  The local server middleware is assumed to be running locally (127.0.0.1). 

### Misty

To test the interface to a Misty robot, try the following:
```
python3 behavior_gen.py --misty --address 192.168.1.3
```
Replace the IP address for the Misty robot. 
