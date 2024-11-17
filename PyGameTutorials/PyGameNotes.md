# Making a game in PyGame!!

## Surfaces 
Need to create a **display surface**, this is our game window 

* Must be unique, is always visible 

Then we have a **regular surface** which is essentially a single image

* This can be something imported, rendered text or a plain colour
* Can have as many regular surfaces as you want
* Only shown when connected to the display surface

To show regular surface on display surface use:
`screen.blit(surface, position)`

where blit stands for Block Image Transfer 

takes 2 arguments, surface we want to show and the position we want it 

In pygame, coordinates for screen start in top left i.e., origin 0,0 is top left
