# 22 - Game, Set and Hash

> Can you beat the tennis master?
>
> hackyeaster.hacking-lab.com:8888

Connecting to the service, we notice that we are supposed to
quickly "reverse" hashes given to us. For this challenge a
python script was created ([game.py](game.py)), looking up each hash using 
http://hashtoolkit.com/.


```
python.exe ./game.py
Got digest: ba4788b226aa8dc2e6dc74248bb9f618cfa8c959e0c26c147be48f6839a0b088
Found cleartext: green
>> Correct! Point for you.

----------------------
Player > 0 15
Master   0 0
----------------------
Got digest: d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1
Found cleartext: pass
>> Correct! Point for you.

----------------------
Player > 0 30
Master   0 0
----------------------
Got digest: 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
Found cleartext: 123456
>> Correct! Point for you.

----------------------
Player > 0 40
Master   0 0
----------------------
Got digest: 38ff0b7c7cc0761a20be0eae460c39c3496f7924177abc89b3d37e8e274763aa
Found cleartext: sarita
>> Correct! Point for you.

----------------------
Player   1 0
Master > 0 0
----------------------
Got digest: b2ecdfeaf5ad92c878e7a5abd02287791c7af3760db6aab8ab1f262afbb4987d
Found cleartext: babyd532
>> Correct! Point for you.

----------------------
Player   1 15
Master > 0 0
----------------------
Got digest: 17f5ed8682778f62b20a06684b7e41e5270ef5d69f1e082ec7bfb942d253425a
Found cleartext: luvdrama7
>> Correct! Point for you.

----------------------
Player   1 30
Master > 0 0
----------------------
Got digest: 23f0d1232fe15fe55fc778d07f29c4ddbc0ef867f1d11545cd5acdebb366e0c2
Found cleartext: hardcore810
>> Correct! Point for you.

----------------------
Player   1 40
Master > 0 0
----------------------
Got digest: 249f3b4c5f8c5b5f9b072f1f4daa595c9966cd59a44c7ccaaed69734918ff0b0
Found cleartext: katr0904
>> Correct! Point for you.

----------------------
Player > 2 0
Master   0 0
----------------------
Got digest: d2a1ba788399c8d1c1273791c5d9937a0b844247425556a9464677ac6dbbbd1f
Found cleartext: morgan
>> Correct! Point for you.

----------------------
Player > 2 15
Master   0 0
----------------------
Got digest: 44c59909f17c296d6f2ec4a53efac3a951add75aa67616d9c5d9d2f5fbb44f04
Found cleartext: 2112
>> Correct! Point for you.

----------------------
Player > 2 30
Master   0 0
----------------------
Got digest: 61bffea9215f65164ad18b45aff1436c0c165d0d5dd2087ef61b4232ba6d2c1a
Found cleartext: richard
>> Correct! Point for you.

----------------------
Player > 2 40
Master   0 0
----------------------
Got digest: ce1484f50441f993b211de372a6968e3c424604c985829f96f3050323437df99
Found cleartext: dolphins
>> Correct! Point for you.

----------------------
Player   3 0
Master > 0 0
----------------------
Got digest: 8f291d2f7575ed651fcbbb810b335f42e63782bbf78170bafbf960c6b703c153
Found cleartext: bettydahdul
>> Correct! Point for you.

----------------------
Player   3 15
Master > 0 0
----------------------
Got digest: 6a74e6e2c082908af95d704c51889d0227962a57d3eae6fc1e343035449024e7
Found cleartext: kristhaiz
>> Correct! Point for you.

----------------------
Player   3 30
Master > 0 0
----------------------
Got digest: 637ab06cc899d01277a66f775440f0e138524f666693213239c9e076840f2e35
Found cleartext: sady7110
>> Correct! Point for you.

----------------------
Player   3 40
Master > 0 0
----------------------
Got digest: 82af9d01d3fff00051fcf912111d83110dd9a2c658ecf109ff26aa7522c02212
Found cleartext: keesjan
>> Correct! Point for you.

----------------------
Player > 4 0
Master   0 0
----------------------
Got digest: 06b9a6eacd7a77b9361123fd19776455eb16b9c83426a1abbf514a414792b73f
Found cleartext: jason
>> Correct! Point for you.

----------------------
Player > 4 15
Master   0 0
----------------------
Got digest: 08798cf02c3644a38d8377ba716ee9cf03aa9218936f3d78075816efbe16cca7
Found cleartext: chris6
>> Correct! Point for you.

----------------------
Player > 4 30
Master   0 0
----------------------
Got digest: 2123f6cda9b8e8b7d8fdd42fabaa5e23c82cce0270201fa74ac408dd5287de6a
Found cleartext: william1
>> Correct! Point for you.

----------------------
Player > 4 40
Master   0 0
----------------------
Got digest: 3b626ba9f29a735b6132bc929ded19f94f4453ebd08fa2d88a338ea885b786fa
Found cleartext: ximena
>> Correct! Point for you.

----------------------
Player   5 0
Master > 0 0
----------------------
Got digest: 52014e03bf93d0221f6a38e690336c473840e055bcf807025095a6d2dd58f0d4
Found cleartext: laneline1
>> Correct! Point for you.

----------------------
Player   5 15
Master > 0 0
----------------------
Got digest: 274093bb588ca0cd6143f288a044b2463ee3f7d37349f1f3ada011b97bae529d
Found cleartext: ositobonito
>> Correct! Point for you.

----------------------
Player   5 30
Master > 0 0
----------------------
Got digest: d4a7748c10d08d741353f3f93759f0e8a25009361fde8a10fbd7b9c21277a4a1
Found cleartext: gatetede4
>> Correct! Point for you.

----------------------
Player   5 40
Master > 0 0
----------------------
Got digest: ccee4f38929f397e99fd5cccaf48d5d586e90cf74d787422fdb6db4bd7196866
Found cleartext: 1645178317
>> Correct! Point for you.

----------------------
Player > 6 0 0
Master   0 0 0
----------------------
Got digest: ce953a0eb08246617b7f849486c4b26a7af37e9d2e8f0e13b3ae1bf0da8a70a2
Found cleartext: print
>> Correct! Point for you.

----------------------
Player > 6 0 15
Master   0 0 0
----------------------
Got digest: 49eff747f7b66f70133bfe00aa8ac2d6b0fbee5be80e52537b0163f147d20418
Found cleartext: thunder
>> Correct! Point for you.

----------------------
Player > 6 0 30
Master   0 0 0
----------------------
Got digest: 56ccc4dcfc96534b06fc0c08a301be24f13b491484d5d984953cc0dba9bbb89a
Found cleartext: please
>> Correct! Point for you.

----------------------
Player > 6 0 40
Master   0 0 0
----------------------
Got digest: 525eca1d5089dbdcbb6700d910c5e0bc23fbaa23ee026c0e224c2b45490e5f29
Found cleartext: star
>> Correct! Point for you.

----------------------
Player   6 1 0
Master > 0 0 0
----------------------
Got digest: 83b756dddef7de4c5b8a6dd498c9366dd3ecc07157b0dbeac5fb7575abd4a986
Found cleartext: metal74
>> Correct! Point for you.

----------------------
Player   6 1 15
Master > 0 0 0
----------------------
Got digest: 10426253a2fcb6db8c40fd0376c95b791bae0973258facd7421e6d9be87e8dc6
Found cleartext: fatassa121690
>> Correct! Point for you.

----------------------
Player   6 1 30
Master > 0 0 0
----------------------
Got digest: 5c530cf90f9890fc7717fc15eee9171a2bed87a45102229c43117b36df5dd3ad
Found cleartext: foursure1
>> Correct! Point for you.

----------------------
Player   6 1 40
Master > 0 0 0
----------------------
Got digest: 4c95731a9f9e14f973e5e7c8dc0665192cd74e6b8034ab7ec3217b854d032eb9
Found cleartext: hatelife16
>> Correct! Point for you.

----------------------
Player > 6 2 0
Master   0 0 0
----------------------
Got digest: 5cc3f82838ba7260203e4590ce03d00e1663d41f6a5167144f5c95d6be2166a0
Found cleartext: office
>> Correct! Point for you.

----------------------
Player > 6 2 15
Master   0 0 0
----------------------
Got digest: 39bd9b8c2185593415bed100ac1cce569343d7078a64a6effa50488d594fdf24
Found cleartext: jesus1
>> Correct! Point for you.

----------------------
Player > 6 2 30
Master   0 0 0
----------------------
Got digest: 75190e3ed9ff3e1cbdb744e5726ece650f5631fb31c7107918b08d8a5a6763cb
Found cleartext: 36633663
>> Correct! Point for you.

----------------------
Player > 6 2 40
Master   0 0 0
----------------------
Got digest: 3fd6b90411449ec718b1fa929c1ba72c52d89f2540c8b3a56ca9cb95fb63d00d
Found cleartext: cookie1
>> Correct! Point for you.

----------------------
Player   6 3 0
Master > 0 0 0
----------------------
Got digest: 359e14bf52c7df25784d0aa568df47acedf4076bd8c3e3bb542b7605c1286232
Found cleartext: westahmunited
>> Correct! Point for you.

----------------------
Player   6 3 15
Master > 0 0 0
----------------------
Got digest: f6643b07c3b1a8d70ebed9ae81bee02204fc3110b32c62e217f28ce9ef44c7d0
Found cleartext: swatchr15
>> Correct! Point for you.

----------------------
Player   6 3 30
Master > 0 0 0
----------------------
Got digest: cde50b525400d17f9ec3d11b1453aea3dca1548f6f2a635e27adafe0c57a8b99
Found cleartext: kemmoli2008
>> Correct! Point for you.

----------------------
Player   6 3 40
Master > 0 0 0
----------------------
Got digest: c4e07a4bd36210543a031428bbe4a48c355267465c9f8edd78159efcc3c18b58
Found cleartext: mojo9230
>> Correct! Point for you.

----------------------
Player > 6 4 0
Master   0 0 0
----------------------
Got digest: e66e9a769d159582cda9c0da24247e36340045a7c340ec59dcd63c0b61cc95cc
Found cleartext: cameron
>> Correct! Point for you.

----------------------
Player > 6 4 15
Master   0 0 0
----------------------
Got digest: 34550715062af006ac4fab288de67ecb44793c3a05c475227241535f6ef7a81b
Found cleartext: michael
>> Correct! Point for you.

----------------------
Player > 6 4 30
Master   0 0 0
----------------------
Got digest: 01a7f7c71074fbf78de6ec86fd26bd9c1f4e1abbbc3b27869ab0fcc04db4106d
Could not determine cleartext
>> Wrong! Point for me.

----------------------
Player > 6 4 30
Master   0 0 15
----------------------
Got digest: 9bfa0b50a90e669907e78780bcc1e5e972742e0d124b30a67fbeb6371c604891
Found cleartext: spider
>> Correct! Point for you.

----------------------
Player > 6 4 40
Master   0 0 15
----------------------
Got digest: 24d9e0d8b353fd0a789ea86f3d33c7ccce3ad547c7612a63d8af4d13dde24d97
Found cleartext: yoteamo
>> Correct! Point for you.

----------------------
Player   6 5 0
Master > 0 0 0
----------------------
Got digest: 7af35e9ab9b9bf2b8806d1595a3c50e0bdb41bd199dc5369264dddf770cfcb22
Found cleartext: 91120158592
>> Correct! Point for you.

----------------------
Player   6 5 15
Master > 0 0 0
----------------------
Got digest: 16a010b86dcd67b6ff35706c78d5c11b0d40f49759d85b19c413092108ea81ce
Found cleartext: tres0me
>> Correct! Point for you.

----------------------
Player   6 5 30
Master > 0 0 0
----------------------
Got digest: cf394620af275389ac3102f1a644db7203e79e55f962aeafd49858520ce22b26
Found cleartext: lia0705
>> Correct! Point for you.

----------------------
Player   6 5 40
Master > 0 0 0
----------------------
Got digest: 95ca3dfde5495fcf893c12c2dbcbd740952554ddde79c2cd409f1e6ac6846da3
Found cleartext: Yethali1980
>> Correct! Point for you.

----------------------
Player > 6 6 0 0
Master   0 0 0 0
----------------------
Got digest: b8510932dad3ddf0fc34661a0caf6674e5c0d672e3930c6a736424d4df0e8016
Found cleartext: ferrari
>> Correct! Point for you.

----------------------
Player > 6 6 0 15
Master   0 0 0 0
----------------------
Got digest: 896860206c0af0d28036cda77c40491ddd484ab14f05b7efb12e31fbf68cc1ec
Found cleartext: 256879
>> Correct! Point for you.

----------------------
Player > 6 6 0 30
Master   0 0 0 0
----------------------
Got digest: 84b0a3665c7d197e977409d425519529ae57667995c6dd4f51d20852ae96a518
Found cleartext: pendejo
>> Correct! Point for you.

----------------------
Player > 6 6 0 40
Master   0 0 0 0
----------------------
Got digest: d68cc2c226778f145f7204b8acca524e498b56bfa69ce9ffad48933ec6d7aff1
Found cleartext: soto
>> Correct! Point for you.

----------------------
Player   6 6 1 0
Master > 0 0 0 0
----------------------
Got digest: de587b51053b7a5ebc686814f8dc7b0464503af3afc1d106e8a20dd79946a011
Found cleartext: $imon1
>> Correct! Point for you.

----------------------
Player   6 6 1 15
Master > 0 0 0 0
----------------------
Got digest: fee709c18b444f1ba582255efa181c6dacab2cc5ee44baacd4ec7d3f4a32ad87
Found cleartext: quin2plet
>> Correct! Point for you.

----------------------
Player   6 6 1 30
Master > 0 0 0 0
----------------------
Got digest: 1faff52e4018662eda00c49bf36e87ed47a36970f4e9bc56d9eb2e216fb115b7
Found cleartext: lorrye
>> Correct! Point for you.

----------------------
Player   6 6 1 40
Master > 0 0 0 0
----------------------
Got digest: 6a0d0e68b0a1ad59afc381d34af28106ce16025f510402dedc746c49bbca9ea8
Found cleartext: keefla1
>> Correct! Point for you.

----------------------
Player > 6 6 2 0
Master   0 0 0 0
----------------------
Got digest: bd9ed22b98e52113fd63d1009b02253a2806af4ec89926083fdc78f0551dd037
Found cleartext: agosto
>> Correct! Point for you.

----------------------
Player > 6 6 2 15
Master   0 0 0 0
----------------------
Got digest: 2fdae8f4af69dec69db47f81e904a64cf38e870636f4ec90b9dbbf24d9678497
Found cleartext: green1
>> Correct! Point for you.

----------------------
Player > 6 6 2 30
Master   0 0 0 0
----------------------
Got digest: 4ea5ee68fea05586106890ded5733820bb77d919cda27bc4b8139b7cd33b8889
Found cleartext: gateway
>> Correct! Point for you.

----------------------
Player > 6 6 2 40
Master   0 0 0 0
----------------------
Got digest: 99bde068af2d49ed7fc8b8fa79abe13a6059e0db320bb73459fd96624bb4b33f
Found cleartext: victor
>> Correct! Point for you.

----------------------
Player   6 6 3 0
Master > 0 0 0 0
----------------------
Got digest: 8e71024836fa25373e3ea8d5bc9be97fe1dc1271e1e6a9f075efaf278a5b576b
Found cleartext: shenethia
>> Correct! Point for you.

----------------------
Player   6 6 3 15
Master > 0 0 0 0
----------------------
Got digest: 49106c1574956ba5e43bca6c827105cd8fb1e03c12a39cb6d4210e16626527af
Found cleartext: LORE20
>> Correct! Point for you.

----------------------
Player   6 6 3 30
Master > 0 0 0 0
----------------------
Got digest: 41dd3e3e160198be45b3e7cdd8e3c7009581dabc7baa99647e0d0c0b1fe5abd4
Found cleartext: accuspec1
>> Correct! Point for you.

----------------------
Player   6 6 3 40
Master > 0 0 0 0
----------------------
Got digest: b9ff6216afbf50a28cc16c5b9e4b5707f76826624918f496d1e57da8f388045c
Found cleartext: 25567416
>> Correct! Point for you.

----------------------
Player > 6 6 4 0
Master   0 0 0 0
----------------------
Got digest: f3c2ce176290b0c384cb4881eb714f2db58f630c33863d91c9bedf58d36007db
Found cleartext: carmen
>> Correct! Point for you.

----------------------
Player > 6 6 4 15
Master   0 0 0 0
----------------------
Got digest: dca6ec9510fc0176c600bb5d75a919fba07877c74eb1a41b0530b330c5767648
Found cleartext: sierra
>> Correct! Point for you.

----------------------
Player > 6 6 4 30
Master   0 0 0 0
----------------------
Got digest: d438483fbb25b8f202cf11c01c11908f33c582e3d95f23366f6600dfd95dbe16
Found cleartext: dantheman
>> Correct! Point for you.

----------------------
Player > 6 6 4 40
Master   0 0 0 0
----------------------
Got digest: f6274d9892026fe47dd5f96f708ef8983dccc7bacf5ee4a90b2400805adaea0a
Found cleartext: merlin
>> Correct! Point for you.

----------------------
Player   6 6 5 0
Master > 0 0 0 0
----------------------
Got digest: a8f963e65945ca1124e1995914108035a711f6771da6923693eb30c562a3cae9
Found cleartext: swieber
>> Correct! Point for you.

----------------------
Player   6 6 5 15
Master > 0 0 0 0
----------------------
Got digest: c33538d270e4ad6196d185116d4db87589b9705e0e17f35b468a61ebc3c1829e
Found cleartext: hallyson00
>> Correct! Point for you.

----------------------
Player   6 6 5 30
Master > 0 0 0 0
----------------------
Got digest: 42dcac8d86042a666151827dcf0418c024d02ed26e78aa0db10799b652d26904
Found cleartext: 162411qw
>> Correct! Point for you.

----------------------
Player   6 6 5 40
Master > 0 0 0 0
----------------------
Got digest: ef50fb962574e5aae2d0c76a10439fe6907347f02a4d4b67a5531343f0abbd34
Found cleartext: 6945340525
>> Correct! Point for you.

----------------------
Player > 6 6 6
Master   0 0 0
----------------------
Got digest: You win! Solution is: !stan-the_marth0n$m4n
```