import os
import requests
import json

class GitHub:

    def __init__(self, username, token,repo_name ):
        self.username = username
        self.token =  token
        self.repo_name = repo_name

    def create_repo(self):
        url = 'https://api.github.com/user/repos'
        data = {
            'name': self.repo_name,
            'private': False,
        }
        headers = {
            'Authorization': 'token {}'.format(self.token),
            'Accept': 'application/vnd.github.v3+json',
        }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == 201:
            return True
        else:
            return False

    def initalize_folder(self):
        os.system("git init")
        os.system("git add .")
        os.system('git commit -m "initial commit" ')
        print(F'git remote add origin https://github.com/{self.username}/{self.repo_name}.git')
        os.system(F'git remote add origin https://github.com/{self.username}/{self.repo_name}.git')
        return True
    

    def push_to_github(self):
        os.system("git push -u origin master")
        return True





        # git remote add origin https://github.com/Adams-Ijachi/next_api.git
        # git remote add origin https://github.com/Adams-Ijachi/next_api.git