# AirBnB clone - The console

## Description of the project
The AirBnB Clone is a project to build a console where we can manipulate objects based on a master class. The data manipulated will be stored in a file using json format.

## Description
The command interpreter or console is a way to connect the user with the program through command lines for different purposes. With this interpreter you can manipulate objects of different classes.

## How to start it
To start the command interpreter, you have to download this repository in your computer and open your terminal. Then, you have to type "./console.py".

example command interpreter :

```
$ ./console.py
(hbnb)
```

## How to use it
It is necessary to call the procedure you want to execute, next is a list of the allowed procedures and how to use them.

-  **create**

	Creates a new instance based on the class name, saves it (to the JSON file) and prints the  `id`. Ex: 

	```
	(hbnb) create BaseModel
	06b5171e-1b27-49c7-8b09-1e8880977148
	```

- **show**

	Prints the string representation of an instance based on the class name and `id`. Ex:

	```
	(hbnb) show BaseModel 06b5171e-1b27-49c7-8b09-1e8880977148
	[BaseModel] (06b5171e-1b27-49c7-8b09-1e8880977148) {'updated_at': datetime.datetime(2020, 2, 19, 14, 4, 27, 608391), 'id': '06b5171e-1b27-49c7-8b09-1e8880977148', 'created_at': datetime.datetime(2020, 2, 19, 14, 4, 27, 608370)}
	```

- **destroy**

	Deletes an instance based on the class name and `id` (save the change into the JSON file). Ex: 

	```
	(hbnb) destroy BaseModel 06b5171e-1b27-49c7-8b09-1e8880977148
	```

- **all**

	Prints all string representation of all instances based or not on the class name. Ex:

	```
	(hbnb) all BaseModel
	["[BaseModel] (06b5171e-1b27-49c7-8b09-1e8880977148) {'id': '06b5171e-1b27-49c7-8b09-1e8880977148', 'created_at': datetime.datetime(2020, 2, 19, 14, 6, 1, 648745), 'updated_at': datetime.datetime(2020, 2, 19, 14, 6, 1, 648765)}"]
	(hbnb) all
	["[BaseModel] (06b5171e-1b27-49c7-8b09-1e8880977148) {'id': '06b5171e-1b27-49c7-8b09-1e8880977148', 'created_at': datetime.datetime(2020, 2, 19, 14, 6, 1, 648745), 'updated_at': datetime.datetime(2020, 2, 19, 14, 6, 1, 648765)}", "[User] (5de3679e-4b93-4a82-8ffd-c35e353b8a66) {'id': '5de3679e-4b93-4a82-8ffd-c35e353b8a66', 'created_at': datetime.datetime(2020, 2, 19, 14, 6, 5, 748583), 'updated_at': datetime.datetime(2020, 2, 19, 14, 6, 5, 748608)}"]
	```

- **update**

	Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). Ex:

	```
	(hbnb) show BaseModel 06b5171e-1b27-49c7-8b09-1e8880977148
	[BaseModel] (06b5171e-1b27-49c7-8b09-1e8880977148) {'updated_at': datetime.datetime(2020, 2, 19, 14, 4, 27, 608391), 'id': '06b5171e-1b27-49c7-8b09-1e8880977148', 'created_at': datetime.datetime(2020, 2, 19, 14, 4, 27, 608370)}
	(hbnb) update BaseModel 06b5171e-1b27-49c7-8b09-1e8880977148 email "aibnb@holbertonschool.com"
	(hbnb) show BaseModel 06b5171e-1b27-49c7-8b09-1e8880977148
	[BaseModel] (06b5171e-1b27-49c7-8b09-1e8880977148) {'created_at': datetime.datetime(2020, 2, 19, 14, 6, 1, 648745), 'updated_at': datetime.datetime(2020, 2, 19, 14, 8, 41, 746116), 'id': '06b5171e-1b27-49c7-8b09-1e8880977148', 'email': 'aibnb@holbertonschool.com'}
	```

- **List of allowed classes**

  - BaseModel.
  - User.
  - State.
  - City.
  - Amenity.
  - Place.
  - Review

## Help

If you want to get information about a command, you can run `help <command>`. Ex:

   ```
   (hbnb) help create
   Creates a new instance of a class
   	Usage: create <name of class>
   (hbnb)
   ```
