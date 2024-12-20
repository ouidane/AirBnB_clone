# AirBnB clone

0x00. AirBnB clone - The console

## Description

This repository represents the foundational phase of a student project aimed at developing an AirBnB website clone. In this phase, a backend interface or console is implemented to handle the management of program data.

## The console

The console offers command-line capabilities for creating, updating, and deleting objects.

## General Use

The following commands are available in the HBnB console:

create - Creates a new instance based on a given class.
destroy - Deletes an object based on its class and UUID.
show - Displays the details of an object based on its class and UUID.
all - Lists all objects the program has access to, or all objects of a specified class.
update - Modifies existing attributes of an object based on its class name and UUID.
quit - Exits the program (the EOF command also functions as an exit).


## Testing :straight_ruler:

Unittests for this project are defined in the [tests](./tests) 
folder. To run the entire test suite simultaneously, execute the following command:

```
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```

## Authors :black_nib:
* **Zakaria Ouidane** <[ZakariaOuidane](https://github.com/ouidane)>
* **Aymen Hommani** <[AymenHommani](https://github.com/Crosspii)>
