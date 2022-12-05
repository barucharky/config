# B"H

## Tools that I'll be working with

### Linking files

This is extremely easy. You just type `link <file1> <file2>` where `file1` is the file you want the link and `file2` is the name of the linked file

Whatever you do to `file1` will happen to `file2` except deletion.

---

### Loop through files in a directory and check if they are a directory

```bash

for i in *;
    do
        if [[ -d "$i" ]]
        then
            echo "$i"
        fi
done

```

---

### Iterate through lines in a file

```bash

file="/path/to/file"

while read line; 
    do
        echo "${line}"

done < "${file}"

```

---

### Recursive file looping

```bash

#!/bin/bash

main_dir="/home/baruch/test/config_dirs"

recurse () {
    for i in *
        do 
            if [ -d $i ]
                then
                    echo "directory: " $i
                    cd $i
                    recurse
                    cd ..
            elif [ -f $i ]
                then
                    echo "file: " $i
            elif [ $i == "*" ]
                then
                    echo "what is $i?"
            fi
    done
}

cd $main_dir
recurse

```

### Double vs. Single brackets in if statements

This is a nuanced issue. Don't investigate too much for this project

https://www.baeldung.com/linux/bash-single-vs-double-brackets

---

### Soft link versus hard link

https://linoxide.com/difference-soft-link-hard-link/

- Soft links can link to a directory, but not an existing directory. 
- Soft links contain pointers, hard links have actual contents

It doesn't seem necessary to link directories because I'm not backing up entire directories, only the config files that I edit

---

### Handling subdirectories in the .config directory

If the directory doesn't exist, it should be created. I will not be creating linked directories. That only leads to problems. 
For example, the .config/Code directory has many files that will not be backed up. 

---


### Recursion

It will be important to understand bash functions well to get the recursion right

https://linuxize.com/post/bash-functions/

functions can have local variables with the same name as variables outside the function without changing them

---

### If, elif, else

Very thorough explanation

https://phoenixnap.com/kb/bash-if-statement