# iterblock2
A wordlist file generator for bruteforcing and dictionary attacks.

Example usage that includes space charactesr and all standard english keyboard characters:

```
python3 iterblock.py ' 1!2@3#4$5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpP[{]}\|aAsSdDffgGhHjJkKlL;:'""'zZxXcCvVbBnNmM,<.>/?' 6
> /mnt/wordlists/6_large.out &
```

Another example in a screenshot with an emoji and a short list of characters:

![iterblock_screenshot](https://keeganbowen.com/images/iterblock_screenshot_1.PNG)


## Disk check feature

If you create a json file in the directory where the script is executed named interblock.json with this in it:

```
{"DISKCHECK": "enable"}
```

Then iterblock.py will call the system shell to check the disk usage of the partition it is running in
and will exit once it reaches 90% usage or greater if that condition is met before the block is fully written to disk. 
This does slow down the file, but creates a disk-aware more cautious option.

## Just right into RAM, okay

Instead of to disk, it can be used to insert into memory. The order of the characters in the first argument dictactes the iteration order.
So if you start your argument with abc, the iterations will start with a as the leading character. This can be used to create threads
with different starting positions, or insert specific strings or groups of strings into memory and then exit, use it in memory, then
shift the argument position order, insert into memory, and repeat etc. So even if you don't have enough disk space, you could generate
chunks and iterate the argument list starting position after testing the wordlist.

```
load1=$(python3 iterblock.py '音~Ѧ🚆1234567890' 3)
```

