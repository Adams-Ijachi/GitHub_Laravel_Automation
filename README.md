# GitHub_Laravel_Automation
 Recently i have had to work with laravel and creating a new repo and new laravel project (* honestly i kept forgetting a the command *) 
 and it was sort of time consuming (something like that) so this script creates a new laravel project, git repo and also pushes it.
 
 ## Prequities
 
 1. [python](https://www.python.org/). Python is need to run the script and also some pip installations
    
 
 2. GitHub Token
    1. Login to your Github account.
    2. Go to Settings -> Developer Settings ->Personal Access Tokens
    3. Click on Generate new token. Confirm your password to continue.
    4. Give any description to your token.
    5. Under scopes check all you want the API to have access to in your account. I checked all the boxes.
    6. Click Generate new token.
    7. tanks to this [meduim post](https://medium.com/analytics-vidhya/getting-started-with-github-api-dc7057e2834d). lot more github endpoints
    
 ## Config
 
 1. First install `pip install requests` so we can make the request to github api
 2. First install `pip install python-dotenv` this so we can have an .evn file in the same root folder as create.py
    1. Create A variable in the .evn called `GITHUB_USERNAME=`
    2. Create A variable in the .evn called `GITHUB_TOKEN=`
    * You don't need to use and env file it's just safer soo yeah, you could go to create.py and hardcode your username and token still works
 
## How to run

1. You can run this by opening the root directory (where the create.py is) and running `python create.py name-of-project -repo -push -vs -lara` (this creates a laravel project, a github repo , and make an initial push to main)
   
2. You will be prompted to **Enter a path :** give a path you want your project to be created ,repo created or pushed

## Command Flags 

1. ` python create.py name-of-project -repo` creates and initializes a repo with the name of project (please ensure the name is unique which means you have no other repo with the same name)
2. ` python create.py name-of-project -repo -push` -push pushes the repo (-push must be used with -repo)
3. `python create.py name-of-project -vs` this opens up vs after script is run
4. `python create.py name-of-project -lara ` this creates a laravel project 
5. `python create.py name-of-project -repo -push -vs -lara` creates, initializes , pushes and opens up vscode

---------

***I hope this helps !!!*** you could just ignore all this and create a project the normal way but what's the fun in that.
 
 
 
 
