You're advised to run the examples using the dockfile, that is,
build an image and run t he container. Example:

```
# from within the project folder ...
sudo docker build . -t my-blog
# to run the container ...
sudo docker run --rm -p 5000:5000 my-blog
# be sure /etc/hosts has dv as an alias to 127.0.0.1
```

Now you need to create the database for the container
using an migration, like this:

```
# get the container id with this command
sudo docker ps
# connect to the running container
sudo docker exec -it <CONTAINER-ID> sh
# run the migration
flask db upgrade
```

You're now ready to try out the example. Cheers!