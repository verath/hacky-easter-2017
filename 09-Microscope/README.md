# 09 - Microscope

This was an app level. In the app we are shown an image with an egg in it, only it is way too small for us to read. Looking through `challenge09.html` in the .apk we see that clicking the "Show Microscope" button opens up an android activity called "microscope".

```html
<p>In order to see this easter egg, you have to look closely!</p>
<p>
  <a href="ps://microscope">
      <button type="button" class="downloadButton">Show Microscope</button>
  </a>
</p>
```

Looking trough the decompiled smali code for the activity (`smali/ps/hacking/hackyeaster/android/MicroscopeActivity.smali`) we see that it opens a WebView set to a URL. The URL is hardcoded, but very slightly obfuscated by replacing the char '6' by '5' before opening it. The relevant smali code looks like this:

```
.line 31
const-string v0, "https://hackyeaster.hacking-lab.com/hackyeaster/challenge09_su6z47IoTT7.html"

.line 32
.local v0, "url":Ljava/lang/String;
const/16 v2, 0x36

const/16 v3, 0x35

invoke-virtual {v0, v2, v3}, Ljava/lang/String;->replace(CC)Ljava/lang/String;

move-result-object v2

invoke-virtual {v1, v2}, Landroid/webkit/WebView;->loadUrl(Ljava/lang/String;)V
```

Visiting the URL in a browser, https://hackyeaster.hacking-lab.com/hackyeaster/challenge09_su5z47IoTT7.html, it is easy to enlargen the embedded image by simply opening it in a new tab.
