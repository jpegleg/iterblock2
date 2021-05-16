# iterblock2
A wordlist file generator for bruteforcing and dictionary attacks.

Example usage:

```
python3 iterblock.py '1!2@3#4$5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpP[{]}\|aAsSdDffgGhHjJkKlL;:'""'zZxXcCvVbBnNmM,<.>/?' 6
> /mnt/wordlists/6_large.out &
```

Another example in a screenshot with an emoji and a short list of characters:

![iterblock_screenshot](https://keeganbowen.com/images/iterblock_screenshot_1.PNG)


## Disk check feature

If you create a json file in the directory where the script is executed with this in it:

```
{"DISKCHECK": "enable"}
```

Then iterblock.py will call the system shell to check the disk usage of the partition it is running in
and will exit once it reaches 90% usage or greater. This does slow down the file, but creates a 
disk-aware more cautious option.

