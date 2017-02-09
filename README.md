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

Once you've signed into your AWS account, navigate to the [ECS console](https://console.aws.amazon.com/ecs/home?region=us-east-1#/clusters).  If you've never used ECS before, you can use the [first run wizard](https://console.aws.amazon.com/ecs/home#/firstRun) which will set up your cluster, a dummy service, and a VPC for you.  If you don't want to use the wizard, you can use the Cloudformation template included in this repo.  
