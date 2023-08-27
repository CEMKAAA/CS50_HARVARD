#                                                   git clone
#command: git clone {https of the repository}. with this command you will download the git repository to your local environment
#
#                                                   git init
#command: git init. we create a git repository in our local environment that we will add files init and send them to actual repository in the internet
#
#                                                   git add
#command: git add {file_name}. we add files to our snapshots snapshots are the changed files that we send with commits to the repositories what we add to snapshots with add will be changed with the previous ones after the commit
#
#                                                   git commit
#command: git commit -m "message to send with commit". we sent our changed file to our local repository that we have created with git init
#
#                                                    git status
#command: this command will inform you if there is some unadded changes inside your files in conclusion it will inform you about unmade changes
#
#                                                    git remote -v
#command: git remote -v. this command will show you the online repositories that you want to push your code if there is empty than your pushes will not work because you still dont set online repository to push your codes
#
#                                                    git push
#command: git push -u {repository_name in git hub online} {branch name in the local environment}
#
#                                                  set url {branch_name}
#command: git remote set-url {repository name} {https url of the repository in the git hub}. in conclusion you say computer make pushes to this https and the specified repository so when you say git push just git push the desired changes will be made to the desired projects desired repository
#
#
#                                                 remote add {online repository name}
#command: git remote add {branch_name} {https url of the git hub repository} this will open a repository in git hub online
#
#                                              pull {online repository name} {online branch name}
#command: git pull origin master. if online repositories desired branch includes a file that you don`t have in your local environment than you can easily pull from the online repository and get the unexisting files in order to push your changes otherwise you will not be able to make changes since online repository includes a file that your local system does not.
#
#                                                  git commit -am "message"
#command: git commit -am "message". with this code without making git add . and then git commit -m "message" this command will allow you to do this both command into just one command git commit -am "message" tadaaaa
#
#                                                  Merge Conflicts
#Now here is the conflict scenerio you have made a change at one file and another person made a change at the same file when you try to pull the project from online repository the git`s system will ask you do you want to get what this another man recently changed or do you want to keep your changes or do you want to merge this two changes this is completely on you
# 
#                                         Here is how git system informs abput the conflict
#        Your changes 
#        <h1>Welcome to my website!!</h1>
#=======
#        Other person`s changes         
#       <h1 style="color: red; text-align:center;font-family: Arial; font-weight: bold;">Welcome to my website</h1>
#>>>>>>> 40a706f380ef3dd6b70bdb32cd90d3ea37fe49bd
#        At this point it is completely on you to decide whether to keep your changes or get the changes that other person has made or you can merge them