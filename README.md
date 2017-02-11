# Getting started with ECS

##Overview of workshop##
This workshop introduces the basics of working with [ECS](https://aws.amazon.com/ecs/).  This includes:  setting up the initial ECS cluster, and deploying two services, with traffic routed through an [ALB](https://aws.amazon.com/elasticloadbalancing/applicationloadbalancer/).

Prior to beginning the workshop, you'll need to complete a few set up steps: 

    [Have a working AWS account](<https://aws.amazon.com>)
    ![Have a working Github account](<https://www.github.com>)
    ![Install the AWS CLI](<http://docs.aws.amazon.com/cli/latest/userguide/installing.html>)
    ![Have Docker installed locally](<https://docs.docker.com/engine/installation/>)

To check if you have the AWS CLI installed:

    $ aws cli
    
This should return something like:

    ➜  ecs-demo git:(master) ✗ aws cli
    usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]

To check if you have Docker installed:

    $  which docker

This should return something like:

    $ vagrant@vagrant:/vagrant$ which docker
    /usr/bin/docker


Once you've completed these steps, you're ready to start the workshop!


##Setting up the VPC

Once you've signed into your AWS account, navigate to the [ECS console](https://console.aws.amazon.com/ecs/home?region=us-east-1#/clusters).  If you've never used ECS before, you can use the [first run wizard](https://console.aws.amazon.com/ecs/home#/firstRun) which will set up your cluster, a dummy service, and a VPC for you.  If you don't want to use the wizard, you can use the [Cloudformation template included in this repo](https://github.com/abby-fuller/ecs-demo/blob/master/ecs-demo-cf.yml), and create a new VPC.

Running the Cloudformation template or the first run wizard should result in something like this:

![cloudformation output](https://github.com/abby-fuller/ecs-demo/blob/master/images/cloudformation_output.png)

##Setting up your IAM roles

In order to work with the AWS CLI, you'll need an IAM role with the proper permissions set up.  To do this, we'll create both an IAM Group, and an IAM user.

To create the group, naviate to the IAM console, and select **Groups** > **Create New Group**.  Name the group "**ecs-demo**".  From the list of managed policies, add the following policies:

![add IAM group](https://github.com/abby-fuller/ecs-demo/blob/master/images/ecs_demo_iam_role.png)

Once you've created your group, you need to attach it to a user.  If you already have an existing user, you can add it to the ecs-group.  If you don't have a user, or need to create a new one, you can do so by going to **Users** > **Add User**:

![add new user](https://github.com/abby-fuller/ecs-demo/blob/master/images/new_iam_user.png)

Name your user something like "**ecs-demo-user**".  From the next step in the wizard, add your user to the "**ecs-demo**" group that we created in the previous step:

![add user to group](https://github.com/abby-fuller/ecs-demo/blob/master/images/add_user_iam_group.png)

When the wizard finishes, make sure to copy or download your access key and secret key.  You'll need them in the next step.

##Configuring the AWS CLI

If you've never configured the AWS CLI, the easiest way is by running:

    $ aws configure

This should drop you into a setup wizard:

    vagrant@vagrant:~/.aws$ aws configure
    AWS Access Key ID [****************K2JA]: 
    AWS Secret Access Key [****************Oqx+]: 
    Default region name [us-east-1]: 
    Default output format [json]: 

If you already have a profile setup with the AWS CLI, you can also add a new profile to your credentials file.

You can test that your IAM user has the correct permissions, and that your CLI is setup to connect to your AWS account by running the command to obtain an ECR authentication token.  This will allow us to pull our registries in the next step:

    $ aws ecr get-login --region us-east-1

This should output something like:

    $ docker login -u AWS -p AQECAHhwm0YaISJeRtJm5n1G6uqeekXuoXXPe5UFce9Rq8/14wAAAy0wggMpBgkqhkiG9w0BBwagggMaMIIDFgIBADCCAw8GCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM+76slnFaYrrZwLJyAgEQgIIC4LJKIDmvEDtJyr7jO661//6sX6cb2jeD/RP0IA03wh62YxFKqwRMk8gjOAc89ICxlNxQ6+cvwjewi+8/W+9xbv5+PPWfwGSAXQJSHx3IWfrbca4WSLXQf2BDq0CTtDc0+payiDdsXdR8gzvyM7YWIcKzgcRVjOjjoLJpXemQ9liPWe4HKp+D57zCcBvgUk131xCiwPzbmGTZ+xtE1GPK0tgNH3t9N5+XA2BYYhXQzkTGISVGGL6Wo1tiERz+WA2aRKE+Sb+FQ7YDDRDtOGj4MwZ3/uMnOZDcwu3uUfrURXdJVddTEdS3jfo3d7yVWhmXPet+3qwkISstIxG+V6IIzQyhtq3BXW/I7pwZB9ln/mDNlJVRh9Ps2jqoXUXg/j/shZxBPm33LV+MvUqiEBhkXa9cz3AaqIpc2gXyXYN3xgJUV7OupLVq2wrGQZWPVoBvHPwrt/DKsNs28oJ67L4kTiRoufye1KjZQAi3FIPtMLcUGjFf+ytxzEPuTvUk4Xfoc4A29qp9v2j98090Qx0CHD4ZKyj7bIL53jSpeeFDh9EXubeqp6idIwG9SpIL9AJfKxY7essZdk/0i/e4C+481XIM/IjiVkh/ZsJzuAPDIpa8fPRa5Gc8i9h0bioSHgYIpMlRkVmaAqH/Fmk+K00yG8USOAYtP6BmsFUvkBqmRtCJ/Sj+MHs+BrSP7VqPbO1ppTWZ6avl43DM0blG6W9uIxKC9SKBAqvPwr/CKz2LrOhyqn1WgtTXzaLFEd3ybilqhrcNtS16I5SFVI2ihmNbP3RRjmBeA6/QbreQsewQOfSk1u35YmwFxloqH3w/lPQrY1OD+kySrlGvXA3wupq6qlphGLEWeMC6CEQQKSiWbbQnLdFJazuwRUjSQlRvHDbe7XQTXdMzBZoBcC1Y99Kk4/nKprty2IeBvxPg+NRzg+1e0lkkqUu31oZ/AgdUcD8Db3qFjhXz4QhIZMGFogiJcmo= -e none https://<account_id>.dkr.ecr.us-east-1.amazonaws.com
 
To login to ECR, copy and paste that output.  That should return something like:

    WARNING: login credentials saved in /home/vagrant/.dockercfg.
    Login Succeeded

Note:  if you are running Ubuntu, it is possible that you will need to preface your Docker commands with `sudo`.  For more information on this, see the [Docker documentation](https://docs.docker.com/engine/installation/linux/ubuntu/).

If you are unable to login to ECR, check your IAM user group permissions.


##Creating the container registries with ECR

Before we can build and push our images, we need somewhere to push them to.  In this case, we're going to create two repositories in [ECR](https://aws.amazon.com/ecr/).

To create a repository, navigate to the ECS console, and select **Repositories**.  From there, choose **Create repository**.

Name your first repository **ecs-demo-web**:

![create ecr repository](https://github.com/abby-fuller/ecs-demo/blob/master/images/ECR_repo_setup.png)

Once you've created the repository, it will display the push commands.  Take note of these, as you'll need them in the next step.  The push commands should like something like this:

![push commands](https://github.com/abby-fuller/ecs-demo/blob/master/images/push_commands.png)

Once you've created the ecs-demo-web, repeat the process for a second repository.  This one should be named **ecs-demo-api**.  Take note of the push commands for this second repository, also.  Push commands are unique per repository.


##Prepping our Docker images

If you haven't already, pull this repository:

    $ git pull git@github.com:abby-fuller/ecs-demo.git

Our first step is the build and test our containers locally.  If you've never worked with Docker before, there are a few basic commands that we'll use in this workshop, but you can find a more thorough list in the [Docker "Getting Started" documentation](https://docs.docker.com/engine/getstarted/).

To start your first container, go to the `web` directory in the project:

    $ cd <path/to/project/ecs-demo/web

To build the container:

    $ docker build -t ecs-demo-web .

This should output steps that look something like this:

    vagrant@vagrant:/vagrant/web$ docker build -t ecs-demo-web .
    Sending build context to Docker daemon 4.096 kB
    Sending build context to Docker daemon 
    Step 0 : FROM ubuntu:latest
     ---> 6aa0b6d7eb90
    Step 1 : MAINTAINER abbyfull@amazon.com
     ---> Using cache
     ---> 3f2b91d4e7a9
  
If the container builds successfully, the output should end with something like this:
 
     Removing intermediate container d2cd523c946a
     Successfully built ec59b8b825de
 
To run your container:
 
     $  docker run -d -p 3000:3000 ecs-demo-web
     
To check if your container is running:
 
     $ docker ps 

This should return a list of all the currently running containers.  In this example,  it should just return a single container, the one that we just started:

    CONTAINER ID        IMAGE                 COMMAND             CREATED              STATUS              PORTS                              NAMES
    fa922a2376d5        ecs-demo-web:latest   "python app.py"     About a minute ago   Up About a minute   3000/tcp,    0.0.0.0:3000->3000/tcp   clever_shockley   
  
To test the actual container output:
 
     $ curl localhost:3000/web
     
This should return:

     hi!  i'm served via Python + Flask.  i'm a web endpoint.
 

To test the api container, repeat the same process from the `/api` directory:

    $ cd <path/to/project/ecs-demo/api 
    $ docker build -t ecs-demo-api .
    $ docker run -d -p 5000:5000 ecs-demo-api
    $ curl localhost:5000/api

The API container should return:

    hi!  i'm ALSO served via Python + Flask.  i'm a second web endpoint.


##Pushing our tested images to ECR   

