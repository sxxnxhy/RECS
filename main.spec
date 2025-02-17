# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/Users/syoo/Downloads/RECS/main.py'],
    pathex=[],
    binaries=[],
    datas=[('/Users/syoo/Downloads/RECS/images/*.png', 'images'), ('/Users/syoo/Downloads/RECS/images/train.icns', 'images')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['/Users/syoo/Downloads/RECS/images/train.icns'],
)
app = BUNDLE(
    exe,
    name='main.app',
    icon='/Users/syoo/Downloads/RECS/images/train.icns',
    bundle_identifier=None,
)
