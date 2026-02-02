# Roman_Converter
I made this project based on <a src="https://leetcode.com/problems/roman-to-integer/description/">leetcode 13</a>.<br>
It was all written in python, so i could create the UI using <a src="https://tkinter.com/">tkinter</a> library.</br>
The code was converted to an executable file in linux in my machine, i'll add it here sooner with a tutorial of how to download it.

## How to use
<ol>
  <li> run the main.py file (must have python3 installed)</li>
  <li> click in the "digits" to write the number you want</li>
  <li> if you miswrote the number, click in the number display</li>
  <li> click the arrow to convert the number</li>
</ol>


## Technologies
<ul>
  <li> Python </li>
  <li> GIMP</li>
</ul>

## Frontend
The background image is the "guide" that leads the fronted code, I designed it on gimp so I could make it quick and simple, since it's not a complex project, while designing i mapped where the buttons would be and drew them all in the image file, so I would'nt need to create button classes on tkinter, it was used mostly to create the window and bind the mouse click.</br>
Since there's no actual buttons, I just had to get the position of the clicks on the screen and add the matching letter to a string.</br>
There's something in the UI that weren't very explicit, once I didn't designed an delete button, the user can "clear" the number it's written by clicking in the top box/area.

## Backend
The whole logic since you have the string with the numbers in roman is, using a cache to save the value while the number is "decresing", decide if you want to add or subtract the number from the total 
<pre>
  <code>
    hm = {"I" : 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000}
    cache = 0
    for i in range(0,len(roman)):
        if i!=0:
            if roman[i] != roman[i-1]:
                total = total + cache if hm[roman[i]] < hm[roman[i-1]] else total - cache
                cache = 0
        cache += hm[roman[i]]
    total += cache
  </code>
</pre>
then, print it in the top box
