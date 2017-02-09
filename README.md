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
