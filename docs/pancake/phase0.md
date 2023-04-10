# build the robot

## Requirements

Review the hardware requirements available [here](https://beezy.dev/pancake/#hardware).

The Raspberry Pi PICO might come with pre-soldered pin header. If not, two options:    
- solder the pin header 
- use alligator clip test cable if you don't want to solder

???+ note
    Don't solder the cables directly to the Pi PICO board, use Dupont type cables allowing you to easily change the pin setup without any difficulties. 

## Diagram 

The below diagram shows the basic wiring without the optional components. 

Even if the GPxx are displayed with specific numbers, these could be reassign to any GPxx. This will however require to adapt the code with the new pin numbers. 

???+ warning
    Make sure to properly distribute the power from the battery back towards the L298N module as the pack provides more than 5V.  
    The L298N module is capable of handling up to 12v as an input and distribute a 5v output that would power the Raspberry Pi PICO.   
    Feeding more than 5v to the Raspberry Pi PICO could burn it!

![RC522](../images/pancake-basic-wiring.png)

