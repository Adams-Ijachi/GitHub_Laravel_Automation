import sys
import argparse
import os
import github as g
from dotenv import load_dotenv

load_dotenv()

    # Login to your Github account.
    # Go to Settings -> Developer Settings ->Personal Access Tokens
    # Click on Generate new token. Confirm your password to continue.
    # Give any description to your token.
    # Under scopes check all you want the API to have access to in your account. I checked all the boxes.
    # Click Generate new token.
    # pip install requests

def createLaravelProject(project_dir,project_name):
    # create a laravel project
    print("Creating Laravel project...")
    os.system("composer create-project --prefer-dist laravel/laravel {}  --".format(project_name))
    print("Laravel project created")

    print("Cd into {}".format(project_name))
    path = os.path.join(project_dir, project_name)
    os.chdir(path)

    


    # os.system("cd {}".format(project_name))
    # print("Installing Laravel dependencies...")
    # os.system("composer install")
    # print("Laravel dependencies installed")
    return True
  
def main():
    try:

        parser = argparse.ArgumentParser()
        parser.add_argument("project_name", type=str,help="add the project name of a given number")
        parser.add_argument("-repo", "--repo", help="Create Github repository",action="store_true")
        parser.add_argument("-push", "--push_repo", help="Push to GitHub",action="store_true")
        parser.add_argument("-lara", "--laravel", help="Create Laravel Project",action="store_true")
        parser.add_argument("-vs", "--vs_code", help="Open VsCode",action="store_true")
        args = parser.parse_args()

        if args.project_name:
            print("Project name: {}".format(args.project_name))
            project_dir = input("Enter the path: ")
            os.chdir(project_dir)

    
        if args.laravel:
            print("Project Directory: {}".format(project_dir))
            project = createLaravelProject(project_dir,args.project_name)

        if args.repo:

            # create a github repository
            print("Creating Github repository")
            username = os.getenv("GITHUB_USERNAME")
            token = os.getenv("GITHUB_TOKEN")
        
            git = g.GitHub(username, token, args.project_name)
            repo = git.create_repo()
            if not repo:
                print("Repository not created")
            git.initalize_folder()
            print("Folder Initailized")

            if args.push_repo:
                git.push_to_github()
                print("Repository Pushed")

        if args.vs_code:
            os.system("code .")
        else:
            print("Script Sucessfully Completed")
        
    except:
        print("Something went wrong!")
        sys.exit(1)


if __name__ == "__main__":
    main()
