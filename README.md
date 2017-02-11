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

    ```
    vagrant@vagrant:~/.aws$ aws configure
    AWS Access Key ID [****************K2JA]: 
    AWS Secret Access Key [****************Oqx+]: 
    Default region name [us-east-1]: 
    Default output format [json]: 
    ```

If you already have a profile setup with the AWS CLI, you can also add a new profile to your credentials file.

##

