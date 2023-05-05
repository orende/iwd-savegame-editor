# iwd-savegame-editor

A simple savegame editor for Icewind Dale Enhanced Edition. This is a proof-of-concept showing how to edit binary files to adjust the party's gold amount.
For more extensive savegame editing (such as changing character stats or inventory) you'd need to have handy a database of item id's and you'd need to 
decompress the zlib compressed data chunks throughout the files. 
Also, if you'd rather not figure out the file-format of the savegame files yourself, check out the Gibberlings page on Infinity engine file formats.

## References
* https://gibberlings3.github.io/iesdp/file_formats/index.htm
* https://github.com/NearInfinityBrowser/NearInfinity
* https://github.com/xanthics/infinity_pickpocket_list
* https://www.zlib.net/
