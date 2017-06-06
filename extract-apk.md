Download https://developer.android.com/studio/releases/platform-tools.html

Follow http://stackoverflow.com/a/18003462/2299303


1)
```
$ adb shell pm list packages
[...]
package:ps.hacking.hackyeaster.android
[...]
```

2)

```
$ adb shell pm path ps.hacking.hackyeaster.android
package:/data/app/ps.hacking.hackyeaster.android-1/base.apk
```

3)

```
$ adb pull /data/app/ps.hacking.hackyeaster.android-1/base.apk hackyeaster.apk
```

4)
Download APKTools, https://ibotpeaches.github.io/Apktool/

```
$ apktool d hackyeaster.apk
I: Using Apktool 2.2.2 on hackyeaster.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: C:\Users\...\AppData\Local\apktool\framework\1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
```