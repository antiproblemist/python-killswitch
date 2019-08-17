# Python Killswitch 

This is a fun project which uses [sdelete](https://docs.microsoft.com/en-us/sysinternals/downloads/sdelete) to securely delete files by reading the file/folder paths from a text file. By default sdelete is set to 3 passes to make the files irrecoverable


### Prerequisite

This code requires [Python](https://www.python.org/downloads/) >=2.7 on a windows system to run

### See it in action
Clone this repository into a folder using `git clone` command
Create file with the name `list.txt` which will contain the files/folders to delete
Each file/folder will be seperated by a new line
Then run the following command
```sh
python secure-delete.py
```

### License
- [BSD 3-clause "New" or "Revised" License](LICENSE)
- [sdelete EULA](Eula.txt)

### Author
Follow the author on [Linkedin](https://www.linkedin.com/in/shahzebq)

**Free Software, Hell Yeah!**
