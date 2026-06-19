[app]
title = Calculator
package.name = calculator
package.domain = org.nabeel
version = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_dirs = tests,bin,__pycache__

[app:android]
android.api = 31
android.minapi = 21
android.ndk = 25.1.8937393
android.archs = arm64-v8a
android.permissions = INTERNET
android.orientation = portrait
android.enable_androidx = True
android.icon = %(source.dir)s/app.png
android.version_code = 1
android.version_name = 0.1

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = .buildozer
bin_dir = ./bin
