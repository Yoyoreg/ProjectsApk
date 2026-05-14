[app]
# (str) Title of your application
title = HomeStore

# (str) Package name
package.name = homestore

# (str) Package domain (needed for android packaging)
package.domain = com.marcidia.apps1

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let's be more specific)
source.include_exts = py,png,jpg,html,css,js,json,txt

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*, *.png, *.jpg

# (str) Application versioning
version = 0.1

# (list) Application requirements
# أضفت المكتبات اللازمة لعمل الـ WebView والتفاعل مع الأندرويد
requirements = python3,kivy==2.2.1,pyjnius,android

# (str) Custom source folders for requirements
# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, CAMERA, ACCESS_FINE_LOCATION

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) Icon of the application
icon.filename = icon.png

# (str) Presplash of the application
presplash.filename = splash.png

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) List of service to declare
# (list) List of Java classes to add to the android project
#android.add_src = 

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
