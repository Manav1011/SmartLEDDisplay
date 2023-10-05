The idea is to display following information on the  LED panel in real time because the information will be constantly updating

data rs485
data rs232
data cloud
video, text messages, camera image display, RTC(realtime clock)


so the idea is to make 3 clients 

1 - provider (read the data from various places like rs485, rs232, cloud, camera, multimedia, images)

2 - consumer (The huidu app which we'll use to display the data we got from the provider)

3 - dash board (This will be used to control how the content will be display on the LED customizable user)


all 3 of the clients needs to be conneted using a websocket connection and all of them will pass the different real time information to each other


also need to add some user authentication mechanisms like signup and login



So the design should be like


first we'll ask the user what is the screen size for example - 192x160, 1920x1080 etc.


according to that size we'll make a div which will represent the led and place that div in the center 

inside that div we'll place and resizable div which will hold the content 

and when user will resize the div the content on the LED screen will also be resized so users are able to customize how the  content will show on the LED screen

this will happen using websockets which will pass the size of the div from dashboard to the LED in realtime
