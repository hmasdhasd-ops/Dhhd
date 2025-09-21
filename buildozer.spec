[app]
title = Rename Content
package.name = renamecontent
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.ndk_api = 21

# صلاحيات
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE
android.allow_backup = True
android.extra_permissions = android.permission.MANAGE_EXTERNAL_STORAGE