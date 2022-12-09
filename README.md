![](vector.jpg?raw=true "Title")
**note: part of this documentation has been ~~stolen~~ borrowed from my last assignment**

## Description
a simulation, powered by vectors, where you control a ball with the help of your mouse and your 1-3 keys.

## Prerequisites
install pytest and pygame on your computer by using the following command in your terminal (or command prompt/git bash, if you're not a cringe mac/linux user)


> pip install pytest
> 
> pip install pygame


now the pip installer really sucks (super duper hard; it's a gigantic pile of garbage like literally every other command line installer) so you might have to input the following instead:


> pip install pygame --pre


## Usage

### "Gameplay"
press 1 to attract the ball to your mouse


press 2 to repel the ball from your mouse


press 3 to make the ball move erratically


the ball will probably begin to orbit your mouse if you press 1. this is because you're applying a centripetal force onto it. now you probably don't know what that is since you slept through your fysik 2 lectures but basically it's a really good sign that i implemented acceleration correctly.

### Testing
install pytest on your computer by using the following command in your terminal (or command prompt/git bash, if you're not a cringe mac/linux user)

> pip install -U pytest

then add pytest to your PATH. go back to your command prompt (or terminal, ew (unless said terminal is git bash)) and navigate to the /src directory, where you then type the following

> pytest test_vectors.py

if you don't trust my usage of pytest, you can go into the test_vectors.py file and change MANUAL_TESTING to true.
