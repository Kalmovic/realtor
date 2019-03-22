# Project Item Catalog - Udacity
### Full Stack Web Development ND
_______________________
## About

This Project has the objective of showing the list of items (cities) and it's subitems(immobiles or properties), beeing able to do all CRUD (Create, Read, Update, Delete) operations to the items and subtiems of the respective creator when loged in.
This project also covers `images manipulation` (CRUD operations) to display the subitems respective uploaded images.

- You are able to login with Facebook or Goole Login, create, read, update or delete items and subitems. If you are not the creator of an item, you can still create a subitem, but not edit or delete that item. You cannot manage the images files of a subitem when you are not the creator.

## Prerequisites:

- Python 2.7.9
    - You can find the link to the download [here](https://www.python.org/downloads/release/python-279/). Download the file that best fit for you.
- Bootstrap 3.3.7
    - You can find the link to the download [here](http://blog.getbootstrap.com/2016/07/25/bootstrap-3-3-7-released/).
- To see all dependencies of this project, there is the `requirements.txt` file. 
    You can type this command: `pip install -r requirements.txt` and install the dependencies of the actual project.

You can also use Vagrant, a VM that comes with lots of dependencies.

- Vagrant
    - First, download vagrant [here](https://www.vagrantup.com/downloads.html). Download the file that best fit for you.
    - Than, clone the repository from Udacity that contains de VM: git clone http://github.com/<username>/fullstack-nanodegree-vm fullstack
    - Go to the file fullstack, than use the `vagrant up` to execute the VM and later `vagrant ssh` to log into the VM.
    - There, use `cd /vagrant` to access the file that contains the database.
    - See that the database file is there, you can place the folder `Realtor` into the vagrant file.
    - To run the Python file, use `python finalproject.py`

- You can access the JSON page by clicking in the `JSON button`

## Visualization of the image CRUD operations and gallery:

Multiple images can be selected at once:

![upload-realtor](https://user-images.githubusercontent.com/42631135/49486659-7dee1200-f826-11e8-9820-f5b3ee45c658.PNG)

Images are then saved into the property gallery:

![upload-realtor2](https://user-images.githubusercontent.com/42631135/49486780-f48b0f80-f826-11e8-9d7d-dd116494a970.PNG)

Images are then added to the carousel:

![upload-realtor3](https://user-images.githubusercontent.com/42631135/49486810-0cfb2a00-f827-11e8-904c-bcf2ee2dab7f.PNG)

## Future improvements:

- Restructure the code using blueprints to better code visuals
- Make it responsive
- Better style the website
- Add the CSRF Protection to the website
- Add treatment erros like one_or_none()

# Author
- Joseph Torres Kaltenecker
