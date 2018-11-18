## how to avoid login prompt when using git
- launch git bash shell
- cd ~
- ssh-keygen
- cat .ssh/id_rsa.pub
- login to github > Profle > Setting
  - add SSH Key with content from .ssh/id_rsa.pub
  
  
## simple git flow to revise one file
- cd /c/GitHub/open_source_learning/projects/Photo_Album/
- git checkout README.md
- git status
- vi README.md
- git add README.md
- git commit -m "plan to leverage this cool project"
- git push origin master

