# Basic Dockerized Backdrop Project

This project allows for easy site development by allowing Docker to take care of running and configuring Apache and MySql. Any themes, profiles, or modules should be placed inside this project's files, layouts, modules, sites, or themes directory.

In order to run multiple Backdrop projects one one machine simply rename the project directory from dockerized_backdrop_cms to the name of the project you're working on. Simply putting the project in another folder will not create a fresh Docker project.

## Installation

### 0. Install Docker
This project uses Docker to manage the installation and configuration of Backdrop's dependencies. Make sure that Docker is installed on your host machine. Installation instructions can be found here: [Mac](https://docs.docker.com/v17.12/docker-for-mac/install/)  |  [Windows](https://docs.docker.com/docker-for-windows/install/)  |  [Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

### 1. Run the installer

To install the Backdrop CMS `cd` into the project directory and run

```
./install.sh
```
in the terminal.

Python 3 is required for the installer to run.

### 2. Build the project.

In order to use this project it must be built in the terminal. 

Use:

```
$ docker-compose build
```

The build step will take awhile as it configures the container to meet Backdrop's requirements. Ideally this step is only necessary once -- unless of course the container is deleted.

### 2. Launch the projecct.

Use:

```
$ docker-compose up
```

In order to launch the project. 

Anytime you want to shutdown the container use `ctrl-c` to stop the process. Use `docker-compose up` again to launch the container the next time you want to use it.

You will be able to access the Backdrop installation in your browser at `localhost:8085/`

### 3. Set database credentials.

Visit `localhost:8085/` to set up Backdrop.

The database credentials exists in `docker-compose.yml` and have these default values: 

```yml
    environment:
      MYSQL_DATABASE: app
      MYSQL_USER: web
      MYSQL_PASSWORD: pass
```

**Special Note**

It's recommended to change the default database credentials if you choose to use this repo in production somewhere.

**IMPORTANT**

**Before submitting the database credentials proceed to step 4**

### 4. Set the Database Address
The default value `127.0.0.1` won't work and is hidden in the `Advanced` section when filling in the database credentials.
Because the database exists in a separate container this must be changed from `127.0.0.1` to `backdropdb`. This references the container's address in the docker network.

### 5. Rejoice
Now you should be able to finish Backdrop's setup sequence and enter in your site information. 
After this, you should have a fully functional Backdrop installation without the need to install and configure php, apache, and mysql on your host machine. 

**Note**
This project is for creating a dev environment to create and test themes, modules, and profiles. **It does not attempt to solve any update regimes that must be in place on the production server.** Be very careful before implementing this project in a mission critical production environment to avoid issues when updates are released.

## License
MIT