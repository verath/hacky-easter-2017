# 12 - Once Upon a File

This challenge provides you with a .zip file holding a single file `file`.

```
$ file file
file: x86 boot sector; partition 1: ID=0x72, starthead 13, startsector 1920221984, 1816210284 sectors, code offset 0x52, OEM-ID "NTFS    ", sectors/cluster 8, reserved sectors 0, Media descriptor 0xf8, hidden sectors 1, dos < 4.0 BootSector (0x80)
```

Running [binwalk](https://github.com/devttys0/binwalk) recursively on the file:

```
peter@peter-VirtualBox:~/Desktop/once$ binwalk -Me file 

Scan Time:     2017-04-05 21:32:59
Target File:   /home/peter/Desktop/once/file
MD5 Checksum:  dffe98ce0495f890743a335c8004bb71
Signatures:    374

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------

WARNING: Extractor.execute failed to run external extractor 'jar xvf '%e'': [Errno 2] No such file or directory
184320        0x2D000         Zip archive data, at least v2.0 to extract, compressed size: 439156, uncompressed size: 5242880, name: file
623596        0x983EC         End of Zip archive, footer length: 22


Scan Time:     2017-04-05 21:33:01
Target File:   /home/peter/Desktop/once/_file.extracted/file
MD5 Checksum:  48804d4eb672ffe5d686e1e0189bbe81
Signatures:    374

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
1093632       0x10B000        Microsoft Cabinet archive data, 17834 bytes, 1 file
2832320       0x2B37C0        Microsoft Cabinet archive data, 17834 bytes, 1 file
3116030       0x2F8BFE        Microsoft executable, MS-DOS
3788479       0x39CEBF        mcrypt 2.2 encrypted data, algorithm: blowfish-448, mode: CBC, keymode: 8bit
3793983       0x39E43F        mcrypt 2.2 encrypted data, algorithm: blowfish-448, mode: CBC, keymode: 8bit
4477995       0x44542B        mcrypt 2.2 encrypted data, algorithm: blowfish-448, mode: CBC, keymode: SHA-1 hash
5073287       0x4D6987        mcrypt 2.2 encrypted data, algorithm: blowfish-448, mode: CBC, keymode: 8bit
5075359       0x4D719F        mcrypt 2.2 encrypted data, algorithm: blowfish-448, mode: CBC, keymode: 8bit
5173248       0x4EF000        PNG image, 480 x 480, 8-bit colormap, non-interlaced
5173767       0x4EF207        Zlib compressed data, best compression


Scan Time:     2017-04-05 21:33:04
Target File:   /home/peter/Desktop/once/_file.extracted/_file.extracted/egg12.png
MD5 Checksum:  102c160b6c7ddfe260a67d9c08fb4a15
Signatures:    374

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 480 x 480, 8-bit colormap, non-interlaced
786           0x312           Zlib compressed data, best compression


Scan Time:     2017-04-05 21:33:04
Target File:   /home/peter/Desktop/once/_file.extracted/_file.extracted/eg	Z2.png
MD5 Checksum:  d41d8cd98f00b204e9800998ecf8427e
Signatures:    374

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------


Scan Time:     2017-04-05 21:33:04
Target File:   /home/peter/Desktop/once/_file.extracted/_file.extracted/4EF207
MD5 Checksum:  9255f161e4666994c2974bf83f15f0f1
Signatures:    374

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------


Scan Time:     2017-04-05 21:33:04
Target File:   /home/peter/Desktop/once/_file.extracted/_file.extracted/_egg12.png.extracted/312
MD5 Checksum:  4d6997b5da7a39c817325df523ca9bd5
Signatures:    374

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------

```

In the extracted folder we find a file "egg12.png", which we scan to complete the level.

[egg12](egg12.png)
