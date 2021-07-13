# Keyence-SR2000

## Hardware and Software Setup

### Hardware setup

Plug the ethernet cable into the PC’s ethernet port

### Software setup

Set the wired settings as follows

* IP Address: 192.168.100.1
* Netmask: 255.255.255.0

Then check the connection by
```
    $ ping 192.168.100.100
```

Or you can use pytest to test it, it will test barcode scanner ip and socket connection.
```
    $ pytest
```

## How to use SR2000

### Start SR2000
First you need to clone this repo to your workspace and re-catkin make, then you can type below command to ues it.

```
    $ cd [your workspace]/src && git clone git@github.com:kuolunwang/Keyence-SR2000.git
    $ cd [your workspace] && catkin make
    $ roslaunch barcode_reader SR2000.launch
```

### Tune SR-2000’s focus

However, everytime the environment is changed or the distance between barcodes and SR-2000 changes a lot, the focus needs to be re-tune for better scanning accuracy. It takes about 3 seconds to automatically re-adjust the focus and there’s no need to do it again if the environment isn’t changed.

```
    $ rosservice call /tune_focus
```

### Read barcodes

If the barcode is read in 1 seconds, the service return the barcode number in string type and return ‘ERROR’ if not.

```
    $ rosservice call /read_barcode
```