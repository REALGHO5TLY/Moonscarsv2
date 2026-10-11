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

## Full entry and size inventory
- AndroidManifest.xml: 4,876 B
- META-INF/CERT.RSA: 1,529 B
- META-INF/CERT.SF: 4,242 B
- META-INF/MANIFEST.MF: 4,166 B
- META-INF/com.android.games.engine.build_fingerprint: 68 B
- META-INF/com/android/build/gradle/app-metadata.properties: 56 B
- assets/AVConfig.json: 176,220 B
- assets/bin/Data/Managed/Metadata/global-metadata.dat: 9,392,820 B
- assets/bin/Data/Managed/Resources/Newtonsoft.Json.dll-resources.dat: 639 B
- assets/bin/Data/Managed/Resources/mscorlib.dll-resources.dat: 337,563 B
- assets/bin/Data/RuntimeInitializeOnLoads.json: 2,814 B
- assets/bin/Data/ScriptingAssemblies.json: 3,128 B
- assets/bin/Data/boot.config: 178 B
- assets/bin/Data/data.unity3d: 122,432,524 B
- assets/bin/Data/sharedassets1.resource: 50,870,880 B
- assets/bin/Data/sharedassets42.resource: 148,000 B
- assets/bin/Data/sharedassets68.resource: 1,482,592 B
- assets/bin/Data/sharedassets69.resource: 195,360 B
- assets/bin/Data/sharedassets70.resource: 394,976 B
- assets/bin/Data/sharedassets71.resource: 599,776 B
- assets/bin/Data/unity default resources: 1,121,184 B
- assets/bin/Data/unity_app_guid: 36 B
- classes.dex: 202,208 B
- lib/arm64-v8a/libAPKVISION.so: 1,260,104 B
- lib/arm64-v8a/libil2cpp.so: 46,893,960 B
- lib/arm64-v8a/libmain.so: 6,728 B
- lib/arm64-v8a/libunity.so: 25,175,544 B
- lib/armeabi-v7a/libAPKVISION.so: 917,924 B
- lib/armeabi-v7a/libil2cpp.so: 39,816,544 B
- lib/armeabi-v7a/libmain.so: 8,588 B
- lib/armeabi-v7a/libunity.so: 18,246,408 B
- res/De.png: 15,476 B
- res/FN.png: 22,202 B
- res/H-.png: 9,199 B
- res/Iw.png: 15,476 B
- res/K0.png: 5,816 B
- res/Ut.png: 1,831 B
- res/W5.png: 2,972 B
- res/YA.png: 5,816 B
- res/b2.png: 2,972 B
- res/l4.png: 9,199 B
- res/mG.png: 1,831 B
- res/oj.png: 22,202 B
- resources.arsc: 3,048 B

## APKVision configuration binary identification
- First 64 bytes (hex): 0001000000140100000400404744454632dd3bdb0000096c0000062847504f5386fa7b8700005f3000007b1e47535542d0826e2a0000281800000cf848564152
- Printable prefix: b'\x00\x01\x00\x00\x00\x14\x01\x00\x00\x04\x00@GDEF2\xdd;\xdb\x00\x00\tl\x00\x00\x06(GPOS\x86\xfa{\x87\x00\x00_0\x00\x00{\x1eGSUB\xd0\x82n*\x00\x00(\x18\x00\x00\x0c\xf8HVARU\xcf\xc6\xf2\x00\x00\x1eH\x00\x00\t\xcfOS/2'
- ZIP magic: False
- GZIP magic: False

## Input-related readable strings (for locating existing overlay)
### classes.dex
- \`Landroid/view/KeyEvent;\`
- \`$Lcom/vocies61/Moonscars/BuildConfig;\`
- \`Lcom/vocies61/Moonscars/R$color;\`
- \`Lcom/vocies61/Moonscars/R$id;\`
- \`!Lcom/vocies61/Moonscars/R$mipmap;\`
- \`!Lcom/vocies61/Moonscars/R$string;\`
- \`Lcom/vocies61/Moonscars/R$style;\`
- \`Lcom/vocies61/Moonscars/R;\`
- \`UnitySendMessage\`
- \`com.vocies61.Moonscars\`
- \`dispatchKeyEvent\`
- \`nativeUnitySendMessage\`
### lib/arm64-v8a/libAPKVISION.so
- No clear-text matches
### lib/arm64-v8a/libil2cpp.so
- \`SteamAPI_ISteamInput_GetControllerForGamepadIndex\`
- \`SteamAPI_ISteamUtils_ShowGamepadTextInput\`
- \`UnityEngine.TouchScreenKeyboard::set_active(System.Boolean)\`
- \`UnityEngine.TouchScreenKeyboard::SetSelection(System.Int32,System.Int32)\`
- \`UnityEngine.Input::GetKeyDownInt(UnityEngine.KeyCode)\`
- \`UnityEngine.TouchScreenKeyboard::IsInPlaceEditingAllowed()\`
- \`UnityEngine.TouchScreenKeyboard::get_active()\`
- \`UnityEngine.TouchScreenKeyboard::get_canSetSelection()\`
- \`UnityEngine.TouchScreenKeyboard::get_status()\`
- \`UnityEngine.TouchScreenKeyboard::get_canGetSelection()\`
- \`SteamAPI_ISteamUtils_ShowFloatingGamepadTextInput\`
- \`UnityEngine.Event::set_keyCode(UnityEngine.KeyCode)\`
- \`UnityEngine.Input::GetKeyInt(UnityEngine.KeyCode)\`
- \`SteamAPI_ISteamInput_GetGamepadIndexForController\`
- \`SteamAPI_ISteamUtils_GetEnteredGamepadTextInput\`
- \`UnityEngine.TouchScreenKeyboard::get_text()\`
- \`UnityEngine.TouchScreenKeyboard::set_hideInput(System.Boolean)\`
- \`UnityEngine.TouchScreenKeyboard::set_text(System.String)\`
- \`UnityEngine.Event::get_keyCode()\`
- \`SteamAPI_ISteamUtils_GetEnteredGamepadTextLength\`
- \`UnityEngine.TouchScreenKeyboard::set_characterLimit(System.Int32)\`
- \`UnityEngine.TouchScreenKeyboard::GetSelection(System.Int32&,System.Int32&)\`
- \`UnityEngine.Input::GetKeyUpInt(UnityEngine.KeyCode)\`
- \`UnityEngine.TouchScreenKeyboard::Internal_Destroy(System.IntPtr)\`

## Android classes present in the port
- \`Landroidx/loader/app/services/a;\`
- \`Landroidx/loader/app/services/b$a;\`
- \`Landroidx/loader/app/services/b;\`
- \`Landroidx/loader/app/services/c;\`
- \`Landroidx/loader/app/services/d;\`
- \`Landroidx/loader/app/services/e;\`
- \`Landroidx/loader/app/services/f;\`
- \`Landroidx/loader/app/services/g;\`
- \`Landroidx/loader/app/services/h;\`
- \`Landroidx/loader/app/services/i;\`
- \`Landroidx/loader/app/services/j;\`
- \`Landroidx/loader/app/services/k;\`
- \`Landroidx/loader/app/services/l$a;\`
- \`Landroidx/loader/app/services/l$b;\`
- \`Landroidx/loader/app/services/l;\`
- \`Lcom/android/support/BuildConfig;\`
- \`Lcom/android/support/CrashHandler$$ExternalSyntheticLambda0;\`
- \`Lcom/android/support/CrashHandler$$ExternalSyntheticLambda1;\`
- \`Lcom/android/support/CrashHandler$1;\`
- \`Lcom/android/support/CrashHandler;\`
- \`Lcom/android/support/Launcher$1;\`
- \`Lcom/android/support/Launcher;\`
- \`Lcom/android/support/Main;\`
- \`Lcom/android/support/MainActivity;\`
- \`Lcom/android/support/Menu$10;\`
- \`Lcom/android/support/Menu$11;\`
- \`Lcom/android/support/Menu$12;\`
- \`Lcom/android/support/Menu$13;\`
- \`Lcom/android/support/Menu$14;\`
- \`Lcom/android/support/Menu$15;\`
- \`Lcom/android/support/Menu$16$1;\`
- \`Lcom/android/support/Menu$16$2;\`
- \`Lcom/android/support/Menu$16$3;\`
- \`Lcom/android/support/Menu$16;\`
- \`Lcom/android/support/Menu$17$1;\`
- \`Lcom/android/support/Menu$17$2;\`
- \`Lcom/android/support/Menu$17$3;\`
- \`Lcom/android/support/Menu$17;\`
- \`Lcom/android/support/Menu$18$1;\`
- \`Lcom/android/support/Menu$18$2;\`
- \`Lcom/android/support/Menu$18$3;\`
- \`Lcom/android/support/Menu$18;\`
- \`Lcom/android/support/Menu$19;\`
- \`Lcom/android/support/Menu$1;\`
- \`Lcom/android/support/Menu$20;\`
- \`Lcom/android/support/Menu$21;\`
- \`Lcom/android/support/Menu$2;\`
- \`Lcom/android/support/Menu$3;\`
- \`Lcom/android/support/Menu$4;\`
- \`Lcom/android/support/Menu$5;\`
- \`Lcom/android/support/Menu$6;\`
- \`Lcom/android/support/Menu$7;\`
- \`Lcom/android/support/Menu$8;\`
- \`Lcom/android/support/Menu$9;\`
- \`Lcom/android/support/Menu;\`
- \`Lcom/android/support/NativeProxy;\`
- \`Lcom/android/support/Preferences;\`
- \`Lcom/android/support/R$color;\`
- \`Lcom/android/support/R$drawable;\`
- \`Lcom/android/support/R$layout;\`
- \`Lcom/android/support/R$mipmap;\`
- \`Lcom/android/support/R$string;\`
- \`Lcom/android/support/R$style;\`
- \`Lcom/android/support/R;\`
- \`Lcom/google/android/gms/tasks/OnCompleteListener;\`
- \`Lcom/google/android/gms/tasks/OnSuccessListener;\`
- \`Lcom/google/android/gms/tasks/RuntimeExecutionException;\`
- \`Lcom/google/android/gms/tasks/Task;\`
- \`Lcom/google/android/play/core/assetpacks/AssetPackException;\`
- \`Lcom/google/android/play/core/assetpacks/AssetPackLocation;\`
- \`Lcom/google/android/play/core/assetpacks/AssetPackManager;\`
- \`Lcom/google/android/play/core/assetpacks/AssetPackManagerFactory;\`
- \`Lcom/google/android/play/core/assetpacks/AssetPackState;\`
- \`Lcom/google/android/play/core/assetpacks/AssetPackStateUpdateListener;\`
- \`Lcom/google/android/play/core/assetpacks/AssetPackStates;\`
- \`Lcom/google/androidgamesdk/ChoreographerCallback;\`
- \`Lcom/google/androidgamesdk/SwappyDisplayManager;\`
- \`Lcom/google/androidgamesdk/a;\`
- \`Lcom/google/androidgamesdk/b;\`
- \`Lcom/google/androidgamesdk/c;\`
- \`Lcom/google/androidgamesdk/d;\`
- \`Lcom/unity3d/player/A0;\`
- \`Lcom/unity3d/player/A;\`
- \`Lcom/unity3d/player/AudioVolumeHandler;\`
- \`Lcom/unity3d/player/B0;\`
- \`Lcom/unity3d/player/B;\`
- \`Lcom/unity3d/player/BuildConfig;\`
- \`Lcom/unity3d/player/C0;\`
- \`Lcom/unity3d/player/C;\`
- \`Lcom/unity3d/player/Camera2Wrapper;\`
- \`Lcom/unity3d/player/D0;\`
- \`Lcom/unity3d/player/D;\`
- \`Lcom/unity3d/player/E0;\`
- \`Lcom/unity3d/player/E;\`
- \`Lcom/unity3d/player/F0;\`
- \`Lcom/unity3d/player/F;\`
- \`Lcom/unity3d/player/G0;\`
- \`Lcom/unity3d/player/G;\`
- \`Lcom/unity3d/player/GoogleARCoreApi;\`
- \`Lcom/unity3d/player/H0;\`
- \`Lcom/unity3d/player/H;\`
- \`Lcom/unity3d/player/HFPStatus$1;\`
- \`Lcom/unity3d/player/HFPStatus;\`
- \`Lcom/unity3d/player/I0;\`
- \`Lcom/unity3d/player/I;\`
- \`Lcom/unity3d/player/IAssetPackManagerDownloadStatusCallback;\`
- \`Lcom/unity3d/player/IAssetPackManagerMobileDataConfirmationCallback;\`
- \`Lcom/unity3d/player/IAssetPackManagerStatusQueryCallback;\`
- \`Lcom/unity3d/player/IPermissionRequestCallbacks;\`
- \`Lcom/unity3d/player/IUnityPlayerLifecycleEvents;\`
- \`Lcom/unity3d/player/J0;\`
- \`Lcom/unity3d/player/J;\`
- \`Lcom/unity3d/player/K0;\`
- \`Lcom/unity3d/player/K;\`
- \`Lcom/unity3d/player/L0;\`
- \`Lcom/unity3d/player/L;\`
- \`Lcom/unity3d/player/M0;\`
- \`Lcom/unity3d/player/M;\`
- \`Lcom/unity3d/player/MultiWindowSupport;\`
- \`Lcom/unity3d/player/N0;\`
- \`Lcom/unity3d/player/N;\`
- \`Lcom/unity3d/player/NativeLoader;\`
- \`Lcom/unity3d/player/NetworkConnectivity;\`
- \`Lcom/unity3d/player/NetworkConnectivityNougat;\`
- \`Lcom/unity3d/player/O0;\`
- \`Lcom/unity3d/player/O;\`
- \`Lcom/unity3d/player/OrientationLockListener;\`
- \`Lcom/unity3d/player/P0;\`
- \`Lcom/unity3d/player/P;\`
- \`Lcom/unity3d/player/PermissionFragment;\`
- \`Lcom/unity3d/player/PlatformSupport;\`
- \`Lcom/unity3d/player/PlayAssetDeliveryUnityWrapper;\`
- \`Lcom/unity3d/player/Q0;\`
- \`Lcom/unity3d/player/Q;\`
- \`Lcom/unity3d/player/R$color;\`
- \`Lcom/unity3d/player/R$id;\`
- \`Lcom/unity3d/player/R$string;\`
- \`Lcom/unity3d/player/R$style;\`
- \`Lcom/unity3d/player/R0;\`
- \`Lcom/unity3d/player/R;\`
- \`Lcom/unity3d/player/ReflectionHelper;\`
- \`Lcom/unity3d/player/S0;\`
- \`Lcom/unity3d/player/S;\`
- \`Lcom/unity3d/player/SoftInputProvider;\`
- \`Lcom/unity3d/player/T0;\`
- \`Lcom/unity3d/player/T;\`
- \`Lcom/unity3d/player/U0;\`
- \`Lcom/unity3d/player/U;\`
- \`Lcom/unity3d/player/UnityCoreAssetPacksStatusCallbacks;\`
- \`Lcom/unity3d/player/UnityPermissions$ModalWaitForPermissionResponse;\`
- \`Lcom/unity3d/player/UnityPermissions;\`
- \`Lcom/unity3d/player/UnityPlayer$SynchronizationTimeout;\`
- \`Lcom/unity3d/player/UnityPlayer;\`
- \`Lcom/unity3d/player/UnityPlayerActivity;\`
- \`Lcom/unity3d/player/V0;\`
- \`Lcom/unity3d/player/V;\`
- \`Lcom/unity3d/player/W0;\`
- \`Lcom/unity3d/player/W;\`
- \`Lcom/unity3d/player/X0;\`
- \`Lcom/unity3d/player/X;\`
- \`Lcom/unity3d/player/Y0;\`
- \`Lcom/unity3d/player/Y;\`
- \`Lcom/unity3d/player/Z0;\`
- \`Lcom/unity3d/player/Z;\`
- \`Lcom/unity3d/player/a/a;\`
- \`Lcom/unity3d/player/a/b;\`
- \`Lcom/unity3d/player/a/c;\`
- \`Lcom/unity3d/player/a/d;\`
- \`Lcom/unity3d/player/a/e;\`
- \`Lcom/unity3d/player/a/f;\`
- \`Lcom/unity3d/player/a0;\`
- \`Lcom/unity3d/player/a1;\`
- \`Lcom/unity3d/player/a;\`
- \`Lcom/unity3d/player/b0;\`
- \`Lcom/unity3d/player/b1;\`
- \`Lcom/unity3d/player/b;\`
- \`Lcom/unity3d/player/c0;\`
- \`Lcom/unity3d/player/c1;\`
- \`Lcom/unity3d/player/c;\`
- \`Lcom/unity3d/player/d0;\`
- \`Lcom/unity3d/player/d1;\`
- \`Lcom/unity3d/player/d;\`
- \`Lcom/unity3d/player/e0;\`
- \`Lcom/unity3d/player/e1;\`
- \`Lcom/unity3d/player/e;\`
- \`Lcom/unity3d/player/f0;\`
- \`Lcom/unity3d/player/f1;\`
- \`Lcom/unity3d/player/f;\`
- \`Lcom/unity3d/player/g0;\`
- \`Lcom/unity3d/player/g1;\`
- \`Lcom/unity3d/player/g;\`
- \`Lcom/unity3d/player/h0;\`
- \`Lcom/unity3d/player/h1;\`
- \`Lcom/unity3d/player/h;\`
- \`Lcom/unity3d/player/i0;\`
- \`Lcom/unity3d/player/i1;\`
- \`Lcom/unity3d/player/i;\`
- \`Lcom/unity3d/player/j0;\`
- \`Lcom/unity3d/player/j;\`
- \`Lcom/unity3d/player/k0;\`
- \`Lcom/unity3d/player/k;\`
- \`Lcom/unity3d/player/l0;\`
- \`Lcom/unity3d/player/l;\`
- \`Lcom/unity3d/player/m0;\`
- \`Lcom/unity3d/player/m;\`
- \`Lcom/unity3d/player/n0;\`
- \`Lcom/unity3d/player/n;\`
- \`Lcom/unity3d/player/o0;\`
- \`Lcom/unity3d/player/o;\`
- \`Lcom/unity3d/player/p0;\`
- \`Lcom/unity3d/player/p;\`
- \`Lcom/unity3d/player/q0;\`
- \`Lcom/unity3d/player/q;\`
- \`Lcom/unity3d/player/r0;\`
- \`Lcom/unity3d/player/r;\`
- \`Lcom/unity3d/player/s0;\`
- \`Lcom/unity3d/player/s;\`
- \`Lcom/unity3d/player/t0;\`
- \`Lcom/unity3d/player/t;\`
- \`Lcom/unity3d/player/u0;\`
- \`Lcom/unity3d/player/u;\`
- \`Lcom/unity3d/player/v0;\`
- \`Lcom/unity3d/player/v;\`
- \`Lcom/unity3d/player/w0;\`
- \`Lcom/unity3d/player/w;\`
- \`Lcom/unity3d/player/x0;\`
- \`Lcom/unity3d/player/x;\`
- \`Lcom/unity3d/player/y0;\`
- \`Lcom/unity3d/player/y;\`
- \`Lcom/unity3d/player/z0;\`
- \`Lcom/unity3d/player/z;\`
- \`Lcom/vocies61/Moonscars/BuildConfig;\`
- \`Lcom/vocies61/Moonscars/R$color;\`
- \`Lcom/vocies61/Moonscars/R$id;\`
- \`Lcom/vocies61/Moonscars/R$mipmap;\`
- \`Lcom/vocies61/Moonscars/R$string;\`
- \`Lcom/vocies61/Moonscars/R$style;\`
- \`Lcom/vocies61/Moonscars/R;\`
- \`Lorg/fmod/FMODAudioDevice;\`
- \`Lorg/fmod/a;\`

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
