# 04 - Cool Car

This is an app level, with the following description:

> Borat wants to impress the girls. Can you help him find a cool car for this purpose?
> 
> The right car will make the Cool-o-Meter reach its full level.


Starting by looking at the `challenge04.html` source, we see that it queries some weird URL `ps://sensors`, and does so every 2s. This is presumably some special URL defined by the application. The `sensorFeedback` is then seemingly called with the result from the sensors. The results looks to be a json object with two fields `k` and `l`, where `k` seems to be used to decrypt the egg image.

Searching the smali folder for the `ps://sensors`, we see that it is mentioned in the `Activity.smali` file:

```
.field private static final URL_SENSORS:Ljava/lang/String; = "ps://sensors"
```

Looking through the file, we also find a method called `startSensors`. The startSensors method finds a sensor (it seems to be using a "magnetic field sensor type"), asks it for a single value and sets itself (the Activity class) as listener. Looking for the `onSensorChanged` method (the method on a [SensorEventListener](https://developer.android.com/reference/android/hardware/SensorEventListener.html) that is called when a sensor value is available), we find that it looks promising as it contains a string mentioning the sensorFeedback method seen previously:

```
const-string v6, "javascript:sensorFeedback(\'{\"k\": \""

invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

move-result-object v5

invoke-virtual {v5, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

move-result-object v5

const-string v6, "\", \"l\": \""

invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

move-result-object v5

invoke-virtual {v5, v2, v3}, Ljava/lang/StringBuilder;->append(D)Ljava/lang/StringBuilder;

move-result-object v5

const-string v6, "\"}\')"
```

In the above, we see that the value we would be intersted in is the value of `v5`, which is appended to the string making the `k` value. Looking trough the code, we can see that it is by default set to "", but if the value of the sensor (`v2`) is larger than 1000.0 then the `k` is set to `sha1("file:///android_asset/www/index.html")`:

```
.line 180
.local v0, "k":Ljava/lang/String;
const-wide v4, 0x408f400000000000L    # 1000.0

cmpl-double v4, v2, v4

if-ltz v4, :cond_0

.line 181
const-string v4, "file:///android_asset/www/index.html"

invoke-static {v4}, Lps/hacking/hackyeaster/android/Activity;->sha1(Ljava/lang/String;)Ljava/lang/String;

move-result-object v0

.line 183
:cond_0
```

Knowing this, we can simply open up the `challenge04.html` in a browser, open the javascript console and call the `decryptScrambledEggWithKey` with the know key `sha1("file:///android_asset/www/index.html") == d2d109036a07c1080a6e77e8063cebdc155f888b`:

```
> decryptScrambledEggWithKey("d2d109036a07c1080a6e77e8063cebdc155f888b")
```

And the egg on the page is decrypted.
