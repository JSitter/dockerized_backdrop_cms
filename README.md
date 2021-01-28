# Basic Dockerized Backdrop 1.x Project

This project allows for easy site development by allowing Docker to take care of running and configuring Apache and MySql. For ease of use and updating of Backdrop Core, certain folders that contain custom code are separated out of Backdrop's source folder. These directories are `files`, `layouts`, `modules`, `sites`, and `themes`. Custom and contributed code should be placed inside these folders which will appear in this project's folder after installation.

In order to run multiple Backdrop projects one must simply rename the project directory from dockerized_backdrop_cms to your preferred project's name and change the name of the database volume referenced in `docker-compose.yml` from `backdropdb` to something else. Simply putting the project in another folder will not create a fresh Docker project.

## Installation

### 0. Install Docker
This project uses Docker to manage the installation and configuration of Backdrop's dependencies. Make sure that Docker is installed on your host machine. Installation instructions can be found here: [Mac](https://docs.docker.com/v17.12/docker-for-mac/install/)  |  [Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/).

### 1. Run the installer

To install the Backdrop CMS use the terminal and `cd` into the project directory. Then run

```
$ ./install.sh
```

Python 3 is required for the installer to run.

The installer will prompt for your project details including the project name, port number, database username, and database password. The installer will configure the docker-compose.yml file with your project specific details. Backdrop will need to be configured with this information when its first run.

### 1. Launch the project.

Use:

```
$ docker-compose up
```

In order to launch the project. 

Anytime you want to shutdown the container use `ctrl-c` to stop the process. Use `docker-compose up` again to launch the container the next time you want to use it.

You will be able to access the Backdrop installation in your browser at the port that was initially set up at installation at`localhost:{PORT}`.

### 2. Set Backdrop credentials.

Visit `localhost:{PORT}` to set up your backdrop installation.

The database credentials exists in the `docker-compose.yml` under the `environment` section and are set up when the installer is first run: 

```yml
    environment:
      MYSQL_DATABASE: myappname
      MYSQL_USER: myappusername
      MYSQL_PASSWORD: mypassword
```

**Special Note**

**Before submitting the database credentials proceed to step 3**

### 3. Set the Database Address
The default value `127.0.0.1` won't work and is hidden in the `Advanced` section when filling in the database credentials.
Because the database exists in a separate container this must be changed from `127.0.0.1` to the name of your project configured at initial installation. This references the container's address in the docker network and is found in the `docker-compose.yml` file under `MYSQL_DATABASE`.

### 4. Rejoice
Now you should be able to finish Backdrop's setup sequence and enter in your site information. 
After this, you should have a fully functional Backdrop installation without the need to install and configure php, apache, and mysql on your host machine. 

**Note**
This project is for creating a dev environment to create and test themes, and modules. **It does not attempt to solve any update regimes that must be in place on the production server.** Be very careful before implementing this project in a mission critical production environment to avoid issues when updates are released.

## License
MIT