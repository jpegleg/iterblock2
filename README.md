# iterblock2
A wordlist file generator for bruteforcing and dictionary attacks with support for emojis, space characters, all special characters, and other languages.

iterblock2 is roughly 3x slower than crunch: https://github.com/crunchsec/crunch/   however iterblock2 has some different features and can use more types of characters.

Example usage that includes space character and all standard english keyboard characters, every combination of 6,
while additionally measuring the execution time and setting the kernel priority to the default "nice" value to be increased
by 10, deprioritizing it some in the linux kernel scheduler:

```
 
time nice -n 10 python3 iterblock.py " 1\!2@3#4\$5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpP[{]}\|aAsSdDfgGhHjJkKlL;:\"'zZxXcCvVbBnNmM,<.>/\?" 6 > /mnt/wordlists/6_large.out &
 
```

Doublequotes around the first arg allow escaped doublequote and single quotes, as well as anything else as the character string.
Singlequotes around the first arg allow double quotes but single quotes will get ignored if there are two and error if one then.
Some characters you will find you need to escape with a \ character such as double quotes and backticks and sometimes bash special characters.

```
python3 iterblock.py "~\`\!1@2#3$4%5^6&7*8(9)0_-+={[}]|\:;\"\'<,>.?/" 2 

```

It doesn't duplicate the \ backslash characters or any other character in the string because it is cast to a set before use.


Another example in a screenshot with an emoji and a short list of characters and writing a file with all combinations of those, 4 characters long:

![iterblock_screenshot](https://keeganbowen.com/images/iterblock_screenshot_1.PNG)


## Disk check feature and the iterblock.json config

If you create a json file in the directory where the script is executed named interblock.json with this in it:

```
{"DISKCHECK": "enable"}
```
Then iterblock.py will call the system shell to check the disk usage of the partition it is running in
and will exit once it reaches 90% usage or greater if that condition is met before the block is fully written to disk. 
This does slow down the file, but creates a disk-aware more cautious option.


The default is not to use the disk check. If you have the JSON file in place but want it disabled, you will want DISKCHECK set to any other value.
This will use the iterblock.json to not use the disk check mode while having a iterblock.json config in place:


```
{"DISKCHECK": "disableit"}
```


## Just right into RAM, okay

Instead of to disk, it can be used to insert into memory. The order of the characters in the first argument dictactes the iteration order.
So if you start your argument with abc, the iterations will start with a as the leading character. This can be used to create threads
with different starting positions, or insert specific strings or groups of strings into memory and then exit, use it in memory, then
shift the argument position order, insert into memory, and repeat etc. So even if you don't have enough disk space, you could generate
chunks and iterate the argument list starting position after testing the wordlist.

```
load1=$(python3 iterblock.py '音~Ѧ🚆1234567890' 3)
```

