# ICE CREAM MAKER
This is a small game where you simply move an ice cream cone to collect ice cream scoops. Right now, the game has no goals. The plan, however, is to add customers with random orders. And you have to get an ice cream with the exact flavors that the customer wants to get points.

### Author
Tora K. Homme

## Installing pygame
Ensure that python is installed

```bash
  python --version
```

Ensure that PIP is installed

```bash
  pip --version
```

Install pygame 

```bash
  pip install pygame
```

## Run the game
Ensure you are in the ice cream directory

```bash
  cd ice_cream_maker
```

Run simulation

```bash
  python3 manager.py
```

## Key Commands
```To start/restart, press SPACE```

```To exit, press ESC or the X in the top corner. This will show the credits, which will automatically exit after some seconds have passed```

```Move the cone with WASD```


## Note
The game is not done! 
Also, the cone is the "hitbox", so you have to hit the cone with the scoop you want.
Hit the customer with the cone to deliver the icecream. Only correct ice creams will be delivered.
Hit the trash can with the scoops. All scoops on the cone will be thrown away.
When the falling scoops hit the floor, they dissapear. Use this as an advantage to not pick up scoops. But be aware of the trash can in the way.
To score coins(points), deliver ice cream to customers. Customers pay 5 * (number of scoops).


## Future plans
customer wait for a set time before leaving.
-> time based: faster delivery = more coins + rn more scoops = more coins
-> goal: fastest time to get to 300 points
animated customers on the side?
upper customer wants 1-2 scoops
middle customer wants 3-4 scoops
last customer wants 5 scoops


### Credits
All backgrounds are made by Tora K. Homme. Ice cream found at PIXILART. Scoops recoloured by Tora K. Homme. 







