# 08 - Snd Mny

This is an app level. In the app we are shown a text that says "snd mny please I'm begging you!"

Looking trough the `challenge08.html` file, we see pretty much nothing intersting. However, looking trough the activities of the app we find a "SndActivity", which seem intersting. Looking trough our decompiled smali version (`smali/ps/hacking/hackyeaster/android/SndActivity.smali`) we find that the activity is reading the intent that started the activity, looks for a text sent in the `android.intent.extra.TEXT`, sha1 hashes that string and compares it to a hardcoded sha1 hash:

```
.line 25
invoke-virtual {p0}, Lps/hacking/hackyeaster/android/SndActivity;->getIntent()Landroid/content/Intent;

move-result-object v5

.line 26
.local v5, "intent":Landroid/content/Intent;
invoke-virtual {v5}, Landroid/content/Intent;->getAction()Ljava/lang/String;

move-result-object v0

.line 27
.local v0, "action":Ljava/lang/String;
invoke-virtual {v5}, Landroid/content/Intent;->getType()Ljava/lang/String;

move-result-object v8

.line 28
.local v8, "type":Ljava/lang/String;
const-string v9, "android.intent.action.SEND"

invoke-virtual {v9, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

move-result v9

if-eqz v9, :cond_0

if-eqz v8, :cond_0

.line 29
const-string v9, "text/plain"

invoke-virtual {v9, v8}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

move-result v9

if-eqz v9, :cond_0

.line 30
const-string v9, "android.intent.extra.TEXT"

invoke-virtual {v5, v9}, Landroid/content/Intent;->getStringExtra(Ljava/lang/String;)Ljava/lang/String;

move-result-object v7

.line 31
.local v7, "text":Ljava/lang/String;
if-eqz v7, :cond_0

.line 32
const-string v9, "c95259de1fd719814daef8f1dc4bd64f9d885ff0"

invoke-virtual {v7}, Ljava/lang/String;->toLowerCase()Ljava/lang/String;

move-result-object v10

invoke-static {v10}, Lps/hacking/hackyeaster/android/SndActivity;->sha1(Ljava/lang/String;)Ljava/lang/String;

move-result-object v10

invoke-virtual {v9, v10}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
```

It is easily found that the text that produces the specific sha1 hash is "money". With that know, sending an intent is actually as easy as writing the text "money", selecting it, picking share and choosing the SndActivity. Doing so we are rewarded with the egg for this level.
