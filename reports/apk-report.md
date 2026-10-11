# Moonscars Android APK: technical inspection

- Filename: `moonscars-original.apk`
- File size: 225,774,920 bytes
- SHA-256: `fc92f78a4f532ce6c8ce5b7969536896f9d2b1cd4e8f7572d316d11c2d1d3906`
- ZIP entries: 44
- DEX files: classes.dex

## Likely port engine
- **Unity** indicators: assets/bin/Data/, libunity.so, libil2cpp.so

## Native libraries
- `lib/arm64-v8a/libAPKVISION.so` (1,260,104 bytes)
- `lib/arm64-v8a/libil2cpp.so` (46,893,960 bytes)
- `lib/arm64-v8a/libmain.so` (6,728 bytes)
- `lib/arm64-v8a/libunity.so` (25,175,544 bytes)
- `lib/armeabi-v7a/libAPKVISION.so` (917,924 bytes)
- `lib/armeabi-v7a/libil2cpp.so` (39,816,544 bytes)
- `lib/armeabi-v7a/libmain.so` (8,588 bytes)
- `lib/armeabi-v7a/libunity.so` (18,246,408 bytes)

## Top-level and assets overview
- assets: 16 entries
- res: 12 entries
- lib: 11 entries
- META-INF: 5 entries
- AndroidManifest.xml: 1 entries
- classes.dex: 1 entries
- resources.arsc: 1 entries

## Potential control mappings/config resources
- `assets/AVConfig.json` (176,220 bytes)
- `assets/bin/Data/boot.config` (178 bytes)

## APKVision control configuration structure
- Unable to parse AVConfig.json as JSON: 'utf-8' codec can't decode byte 0xdd in position 17: invalid continuation byte

## Android manifest / package information
~~~
package: name='com.vocies61.Moonscars' versionCode='1' versionName='1.0' platformBuildVersionName='15' platformBuildVersionCode='35' compileSdkVersion='35' compileSdkVersionCodename='15'
install-location:'auto'
sdkVersion:'24'
targetSdkVersion:'35'
uses-permission: name='android.permission.INTERNET'
application-label:'Moonscars'
application-icon-120:'res/Ut.png'
application-icon-160:'res/W5.png'
application-icon-240:'res/YA.png'
application-icon-320:'res/l4.png'
application-icon-480:'res/Iw.png'
application-icon-640:'res/oj.png'
application: label='Moonscars' icon='res/W5.png'
launchable-activity: name='com.unity3d.player.UnityPlayerActivity'  label='' icon=''
feature-group: label=''
  uses-gl-es: '0x30000'
  uses-feature-not-required: name='android.hardware.touchscreen'
  uses-feature-not-required: name='android.hardware.touchscreen.multitouch'
  uses-feature-not-required: name='android.hardware.touchscreen.multitouch.distinct'
  uses-feature-not-required: name='android.hardware.type.pc'
main
supports-screens: 'small' 'normal' 'large' 'xlarge'
supports-any-density: 'true'
locales: '--_--'
densities: '120' '160' '240' '320' '480' '640'
native-code: '' 'arm64-v8a' 'armeabi-v7a'

~~~
