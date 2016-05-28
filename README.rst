Download files from S3 
====================================

Setup

::

    $ cd LAPP-Analytics/customer-segmentation

    $ virtualenv env 
    $ . env/bin/activate 
    $ pip install -r install/requirements.txt 

    # Make sure you are using python3 alone 
    $ sudo apt-get install python3-pip
    $ sudo pip3 install virtualenv 
    $ virtualenv-3.5 env 

Install the environment and create the AWS profile. Look at 
$HOME/.downloadfiles.ini 

Running the command 

::

  python3 /bin/download-files update 


The $HOME/.downloadfiles.ini looks like this. 
::
  
  [download-files]
  workspace = /home/user/workspace/segment
  bucket = ccd-lapp-data.fourthlion.in
  prefix = pipeline/logs/segment
  access = <segment-user-access-key>
  secret = <segment-user-secret-key>

To download files
::
  #Help
  $python3 bin/download-files --help
  
  #To start downloading files of a particular day
  $python3 bin/download-files download --month 201605 --day 2016-05-01
  
  #month and day are optional, downloads all the files if not specified


