# Pingtest
This is a program that can continuously run a ping test and has a nice output with a graph. This was designed to test the internet connection uptime.  
This is designed to be run on a linux server. In my circumstance I have used a Raspberry Pi plugged directly into my router. 

![Picture of sample image](sampeImage.jpg "picture of sample image")

## Example
To see an example of this [click here](http://pingtester.chaimstanton.co.uk/) (Note: this is completely static)

## Usage
### Run the program on linux
* In order to run the python program from the terminal and continue with the terminal type
the line 
```nohup python3 pingtest.py &``` then press enter again   
* (However in order to do this you will need to have nohup installed)
* Then navigate to index.php (via web server)

### Kill the python3 process using linux
* Type `ps -aux` to get the process identification numbers 
* Then put type `kill <process number>`

### Dependencies 
* python3 
* A web server with php installed 
* [speedtest-cli](https://pypi.org/project/speedtest-cli/) you can install it with pip `python3 -m pip install speedtest-cli` (other options are available via the link)  

## Licence
* Whilst this project is open source it is completely owned by me.  

## Misc
naming convention `Major.Minor.Release`  
