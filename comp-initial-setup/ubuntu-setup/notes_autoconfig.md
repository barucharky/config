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

### Double vs. Single brackets in if statements

https://www.baeldung.com/linux/bash-single-vs-double-brackets