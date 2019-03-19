{
  'targets': [
    {
      'target_name': 'exokit',
      'conditions': [
        ['"<!(echo $LUMIN)"!="1"', {
          'conditions': [
            ['OS=="win"', {
              'sources': [
                'exokit.cpp',
                'deps/exokit-bindings/bindings/src/*.cc',
                'deps/exokit-bindings/util/src/*.cc',
                'deps/exokit-bindings/browser/src/*.cpp',
                'deps/exokit-bindings/canvas/src/*.cpp',
                'deps/exokit-bindings/nanosvg/src/*.cpp',
                'deps/exokit-bindings/canvascontext/src/*.cc',
                'deps/exokit-bindings/webglcontext/src/*.cc',
                'deps/exokit-bindings/platform/windows/src/*.cpp',
                'deps/exokit-bindings/webaudiocontext/src/*.cpp',
                'deps/exokit-bindings/videocontext/src/*.cpp',
                'deps/exokit-bindings/videocontext/src/win/*.cpp',
                'deps/exokit-bindings/windowsystem/src/*.cc',
                'deps/exokit-bindings/glfw/src/*.cc',
                'deps/exokit-bindings/webrtc/src/*.cc',
                'deps/exokit-bindings/webrtc/src/converters/*.cc',
                'deps/exokit-bindings/webrtc/src/webrtc/*.cc',
                'deps/openvr/src/*.cpp',
                'deps/exokit-bindings/leapmotion/src/*.cc',
              ],
              'include_dirs': [
                "<!(node -e \"console.log(require.resolve('nan').slice(0, -16))\")",
                "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/include')\")",
                "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/core')\")",
                "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/config')\")",
                "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/gpu')\")",
                "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/effects')\")",
                "<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/include')\")",
                "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/include')\")",
                "<!(node -e \"console.log(require.resolve('native-browser-deps').slice(0, -9) + '/lib')\")",
                "<!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/include')\")",
                "<!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/include/webrtc')\")",
                "<!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/include/webrtc/third_party/abseil-cpp')\")",
                "<!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/include/webrtc/third_party/libyuv/include')\")",
                "<!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/headers')\")",
                "<!(node -e \"console.log(require.resolve('leapmotion').slice(0, -9) + '/include')\")",
                '<(module_root_dir)/deps/exokit-bindings',
                '<(module_root_dir)/deps/exokit-bindings/utf8',
                '<(module_root_dir)/deps/exokit-bindings/node',
                '<(module_root_dir)/deps/exokit-bindings/native_app_glue',
                '<(module_root_dir)/deps/exokit-bindings/util/include',
                '<(module_root_dir)/deps/exokit-bindings/bindings/include',
                '<(module_root_dir)/deps/exokit-bindings/canvas/include',
                '<(module_root_dir)/deps/exokit-bindings/browser/include',
                '<(module_root_dir)/deps/exokit-bindings/nanosvg/include',
                '<(module_root_dir)/deps/exokit-bindings/canvascontext/include',
                '<(module_root_dir)/deps/exokit-bindings/webglcontext/include',
                '<(module_root_dir)/deps/exokit-bindings/webaudiocontext/include',
                '<(module_root_dir)/deps/exokit-bindings/videocontext/include',
                '<(module_root_dir)/deps/exokit-bindings/windowsystem/include',
                '<(module_root_dir)/deps/exokit-bindings/glfw/include',
                '<(module_root_dir)/deps/exokit-bindings/webrtc',
                '<(module_root_dir)/deps/openvr/include',
                '<(module_root_dir)/deps/exokit-bindings/leapmotion/include',
              ],
              'library_dirs': [
                "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/windows/glew')\")",
                "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/windows/glfw')\")",
                "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/lib/windows')\")",
                "<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/lib/windows')\")",
                "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/windows')\")",
                "<!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/lib/win64')\")",
                "<!(node -e \"console.log(require.resolve('leapmotion').slice(0, -9) + '/lib/win')\")",
                "<!(node -e \"console.log(require.resolve('native-browser-deps-windows').slice(0, -9) + '/lib2/windows')\")",
                "<!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/lib/windows')\")",
              ],
              'libraries': [
                'opengl32.lib',
                'glew32.lib',
                'glfw3dll.lib',
                'gdiplus.lib',
                'skia.lib',
                'LabSound.lib',
                'avformat.lib',
                'avcodec.lib',
                'avutil.lib',
                'avdevice.lib',
                'swscale.lib',
                'swresample.lib',
                'openvr_api.lib',
                'Leap.lib',
                'libcef.lib',
                'libcef_dll_wrapper.lib',
                'webrtc.lib',
                'peerconnection.lib',
                'create_pc_factory.lib',
                'bbr.lib',
                'winmm.lib',
                'wmcodecdspuuid.lib',
                'secur32.lib',
                'msdmo.lib',
                'dmoguids.lib',
                'Iphlpapi.lib',
              ],
              'copies': [
                {
                  'destination': '<(module_root_dir)/build/Release/',
                  'files': [
                    "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/windows/glew/glew32.dll')\")",
                    "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/windows/glfw/glfw3.dll')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/windows/avformat-58.dll')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/windows/avcodec-58.dll')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/windows/avutil-56.dll')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/windows/avdevice-58.dll')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/windows/avfilter-7.dll')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/windows/postproc-55.dll')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/windows/swscale-5.dll')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/windows/swresample-3.dll')\")",
                    "<!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/bin/win64/openvr_api.dll')\")",
                    "<!(node -e \"console.log(require.resolve('leapmotion').slice(0, -9) + '/lib/win/Leap.dll')\")",
                    "<!(node -e \"console.log(require.resolve('native-browser-deps-windows').slice(0, -9) + '/lib2/windows/libcef.dll')\")",
                    "<!(node -e \"console.log(require.resolve('native-browser-deps-windows').slice(0, -9) + '/lib2/windows/chrome_elf.dll')\")",
                    "<!(node -e \"console.log(require.resolve('native-browser-deps-windows').slice(0, -9) + '/lib2/windows/libEGL.dll')\")",
                    "<!(node -e \"console.log(require.resolve('native-browser-deps-windows').slice(0, -9) + '/lib2/windows/libGLESv2.dll')\")",
                    "<!(node -e \"console.log(require.resolve('native-browser-deps-windows').slice(0, -9) + '/lib2/windows/natives_blob.bin')\")",
                    "<!(node -e \"console.log(require.resolve('native-browser-deps-windows').slice(0, -9) + '/lib2/windows/snapshot_blob.bin')\")",
                    "<!(node -e \"console.log(require.resolve('native-browser-deps-windows').slice(0, -9) + '/lib2/windows/v8_context_snapshot.bin')\")",
                    "<!(node -e \"console.log(require.resolve('native-browser-deps').slice(0, -9) + '/lib/Resources/cef_100_percent.pak')\")",
                    "<!(node -e \"console.log(require.resolve('native-browser-deps').slice(0, -9) + '/lib/Resources/cef_200_percent.pak')\")",
                    "<!(node -e \"console.log(require.resolve('native-browser-deps').slice(0, -9) + '/lib/Resources/cef_extensions.pak')\")",
                    "<!(node -e \"console.log(require.resolve('native-browser-deps').slice(0, -9) + '/lib/Resources/cef.pak')\")",
                    "<!(node -e \"console.log(require.resolve('native-browser-deps').slice(0, -9) + '/lib/Resources/devtools_resources.pak')\")",
                    "<!(node -e \"console.log(require.resolve('native-browser-deps').slice(0, -9) + '/lib/Resources/icudtl.dat')\")",
                  ]
                },
                {
                  'destination': '<(module_root_dir)/build/Release/locales/',
                  'files': [
                    "<!(node -e \"console.log(require.resolve('native-browser-deps').slice(0, -9) + '/lib/Resources/locales/en-US.pak')\")",
                  ]
                },
              ],
              'defines': [
                'NOMINMAX',
                'OPENVR',
                'LEAPMOTION',
                'WRAPPING_CEF_SHARED',
                'WEBRTC_WIN',
              ],
            }],
            ['OS=="linux"', {
              'conditions': [
                ['"<!(node -e \"console.log(process.arch)\")"=="x64"', {
                  'sources': [
                    'exokit.cpp',
                    '<!@(ls -1 deps/exokit-bindings/bindings/src/*.cc)',
                    '<!@(ls -1 deps/exokit-bindings/util/src/*.cc)',
                    '<!@(ls -1 deps/exokit-bindings/browser/src/*.cpp)',
                    '<!@(ls -1 deps/exokit-bindings/canvas/src/*.cpp)',
                    '<!@(ls -1 deps/exokit-bindings/nanosvg/src/*.cpp)',
                    '<!@(ls -1 deps/exokit-bindings/canvascontext/src/*.cc)',
                    '<!@(ls -1 deps/exokit-bindings/webglcontext/src/*.cc)',
                    '<!@(ls -1 deps/exokit-bindings/webaudiocontext/src/*.cpp)',
                    '<!@(ls -1 deps/exokit-bindings/videocontext/src/*.cpp)',
                    '<!@(ls -1 deps/exokit-bindings/videocontext/src/linux/*.cpp)',
                    '<!@(ls -1 deps/exokit-bindings/windowsystem/src/*.cc)',
                    '<!@(ls -1 deps/exokit-bindings/glfw/src/*.cc)',
                    '<!@(ls -1 deps/exokit-bindings/webrtc/src/*.cc)',
                    '<!@(ls -1 deps/openvr/src/*.cpp)',
                  ],
                  'include_dirs': [
                    "<!(node -e \"console.log(require.resolve('nan').slice(0, -16))\")",
                    "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/include')\")",
                    "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/core')\")",
                    "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/config')\")",
                    "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/gpu')\")",
                    "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/effects')\")",
                    "<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/include')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/include')\")",
                    "<!(node -e \"console.log(require.resolve('native-browser-deps').slice(0, -9) + '/lib')\")",
                    "<!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/include')\")",
                    "<!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/include/webrtc')\")",
                    "<!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/headers')\")",
                    '<(module_root_dir)/deps/exokit-bindings',
                    '<(module_root_dir)/deps/exokit-bindings/utf8',
                    '<(module_root_dir)/deps/exokit-bindings/node',
                    '<(module_root_dir)/deps/exokit-bindings/native_app_glue',
                    '<(module_root_dir)/deps/exokit-bindings/util/include',
                    '<(module_root_dir)/deps/exokit-bindings/bindings/include',
                    '<(module_root_dir)/deps/exokit-bindings/canvas/include',
                    '<(module_root_dir)/deps/exokit-bindings/browser/include',
                    '<(module_root_dir)/deps/exokit-bindings/nanosvg/include',
                    '<(module_root_dir)/deps/exokit-bindings/canvascontext/include',
                    '<(module_root_dir)/deps/exokit-bindings/webglcontext/include',
                    '<(module_root_dir)/deps/exokit-bindings/webaudiocontext/include',
                    '<(module_root_dir)/deps/exokit-bindings/videocontext/include',
                    '<(module_root_dir)/deps/exokit-bindings/windowsystem/include',
                    '<(module_root_dir)/deps/exokit-bindings/glfw/include',
                    '<(module_root_dir)/deps/exokit-bindings/webrtc/include',
                    '<(module_root_dir)/deps/openvr/include',
                  ],
                  'library_dirs': [
                    "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/linux/glew')\")",
                    "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/linux/glfw')\")",
                    "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/lib/linux')\")",
                    "<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/lib/linux')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/linux')\")",
                    "<!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/lib/linux64')\")",
                    "<!(node -e \"console.log(require.resolve('native-browser-deps-linux').slice(0, -9) + '/lib4/linux')\")",
                    "<!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/lib/linux')\")",
                  ],
                  'libraries': [
                    '-lGL',
                    '-lGLU',
                    '-lX11',
                    '-lGLEW',
                    '-lglfw3',
                    '-lfontconfig',
                    '-lfreetype',
                    '-lpng16',
                    '-lskia',
                    '-lLabSound',
                    '-lavformat',
                    '-lavcodec',
                    '-lavutil',
                    '-lavdevice',
                    '-lswscale',
                    '-lswresample',
                    '-lopenvr_api',
                    '-luuid',
                    '-lXcursor',
                    '-lXinerama',
                    '-lXxf86vm',
                    '-lXrandr',
                    '-lXi',
                    '-lasound',
                    '-lexpat',
                    '-lcef',
                    '-lcef_dll_wrapper',
                    '-lwebrtc',
                  ],
                  'ldflags': [
                    '-Wl,-Bsymbolic', # required for ffmpeg asm linkage
                    '-Wl,--no-as-needed', # required to prevent elision of shared object linkage

                    "-Wl,-rpath,./../node_modules/native-graphics-deps/lib/linux/glew",
                    "-Wl,-rpath,./../node_modules/native-graphics-deps/lib/linux/glfw",
                    "-Wl,-rpath,./../node_modules/native-canvas-deps/lib/linux",
                    "-Wl,-rpath,./../node_modules/native-audio-deps/lib/linux",
                    "-Wl,-rpath,./../node_modules/native-video-deps/lib/linux/libavformat",
                    "-Wl,-rpath,./../node_modules/native-video-deps/lib/linux/libavcodec",
                    "-Wl,-rpath,./../node_modules/native-video-deps/lib/linux/libavutil",
                    "-Wl,-rpath,./../node_modules/native-video-deps/lib/linux/libavdevice",
                    "-Wl,-rpath,./../node_modules/native-video-deps/lib/linux/libavfilter",
                    "-Wl,-rpath,./../node_modules/native-video-deps/lib/linux/libswscale",
                    "-Wl,-rpath,./../node_modules/native-video-deps/lib/linux/libswresample",
                    "-Wl,-rpath,./../node_modules/native-browser-deps-linux/lib4/linux",
                    "-Wl,-rpath,./../node_modules/native-webrtc-deps/lib/linux",
                    "-Wl,-rpath,./../node_modules/native-openvr-deps/bin/linux64",
                    "-Wl,-rpath,./node_modules/native-openvr-deps/bin/linux64",
                  ],
                  'defines': [
                    'NOMINMAX',
                    'OPENVR',
                    'WRAPPING_CEF_SHARED',
                    'WEBRTC_POSIX',
                  ],
                }],
                ['"<!(node -e \"console.log(process.arch)\")"=="arm64"', {
                  'sources': [
                    'exokit.cpp',
                    '<!@(ls -1 deps/exokit-bindings/bindings/src/*.cc)',
                    '<!@(ls -1 deps/exokit-bindings/util/src/*.cc)',
                    '<!@(ls -1 deps/exokit-bindings/canvas/src/*.cpp)',
                    '<!@(ls -1 deps/exokit-bindings/nanosvg/src/*.cpp)',
                    '<!@(ls -1 deps/exokit-bindings/canvascontext/src/*.cc)',
                    '<!@(ls -1 deps/exokit-bindings/webglcontext/src/*.cc)',
                    '<!@(ls -1 deps/exokit-bindings/webaudiocontext/src/*.cpp)',
                    '<!@(ls -1 deps/exokit-bindings/videocontext/src/*.cpp)',
                    '<!@(ls -1 deps/exokit-bindings/videocontext/src/linux/*.cpp)',
                    '<!@(ls -1 deps/exokit-bindings/windowsystem/src/*.cc)',
                    '<!@(ls -1 deps/exokit-bindings/glfw/src/*.cc)',
                    '<!@(ls -1 deps/exokit-bindings/webrtc/src/*.cc)',
                  ],
                  'include_dirs': [
                    "<!(node -e \"console.log(require.resolve('nan').slice(0, -16))\")",
                    "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/include')\")",
                    "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/core')\")",
                    "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/config')\")",
                    "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/gpu')\")",
                    "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/effects')\")",
                    "<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/include')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/include')\")",
                    '<(module_root_dir)/deps/exokit-bindings',
                    '<(module_root_dir)/deps/exokit-bindings/utf8',
                    '<(module_root_dir)/deps/exokit-bindings/node',
                    '<(module_root_dir)/deps/exokit-bindings/native_app_glue',
                    '<(module_root_dir)/deps/exokit-bindings/util/include',
                    '<(module_root_dir)/deps/exokit-bindings/bindings/include',
                    '<(module_root_dir)/deps/exokit-bindings/canvas/include',
                    '<(module_root_dir)/deps/exokit-bindings/nanosvg/include',
                    '<(module_root_dir)/deps/exokit-bindings/canvascontext/include',
                    '<(module_root_dir)/deps/exokit-bindings/webglcontext/include',
                    '<(module_root_dir)/deps/exokit-bindings/webaudiocontext/include',
                    '<(module_root_dir)/deps/exokit-bindings/videocontext/include',
                    '<(module_root_dir)/deps/exokit-bindings/windowsystem/include',
                    '<(module_root_dir)/deps/exokit-bindings/glfw/include',
                    '<(module_root_dir)/deps/exokit-bindings/webrtc',
                  ],
                  'library_dirs': [
                    "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib2/arm64/glew')\")",
                    "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib2/arm64/glfw')\")",
                    "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/lib2/arm64')\")",
                    "<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/lib2/arm64')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib2/arm64')\")",
                  ],
                  'libraries': [
                    '-lGL',
                    '-lEGL',
                    '-lGLU',
                    '-lX11',
                    '-lGLEW',
                    '-lglfw3',
                    '-lfontconfig',
                    '-lfreetype',
                    '-lpng16',
                    '-lskia',
                    '-lc++_static',
                    '-lLabSound',
                    '-lavformat',
                    '-lavcodec',
                    '-lavutil',
                    '-lavdevice',
                    '-lswscale',
                    '-lswresample',
                    '-luuid',
                    '-lXcursor',
                    '-lXinerama',
                    '-lXxf86vm',
                    '-lXrandr',
                    '-lXi',
                    '-lasound',
                    '-lexpat',
                  ],
                  'ldflags': [
                    '-Wl,-Bsymbolic', # required for ffmpeg asm linkage
                    '-Wl,--no-as-needed', # required to prevent elision of shared object linkage

                    "-Wl,-rpath,./../node_modules/native-graphics-deps/lib2/arm64/glew",
                    "-Wl,-rpath,./../node_modules/native-graphics-deps/lib2/arm64/glfw",
                    "-Wl,-rpath,./../node_modules/native-canvas-deps/lib2/arm64",
                    "-Wl,-rpath,./../node_modules/native-audio-deps/lib2/arm64",
                    "-Wl,-rpath,./../node_modules/native-video-deps/lib2/arm64/libavformat",
                    "-Wl,-rpath,./../node_modules/native-video-deps/lib2/arm64/libavcodec",
                    "-Wl,-rpath,./../node_modules/native-video-deps/lib2/arm64/libavutil",
                    "-Wl,-rpath,./../node_modules/native-video-deps/lib2/arm64/libavdevice",
                    "-Wl,-rpath,./../node_modules/native-video-deps/lib2/arm64/libavfilter",
                    "-Wl,-rpath,./../node_modules/native-video-deps/lib2/arm64/libswscale",
                    "-Wl,-rpath,./../node_modules/native-video-deps/lib2/arm64/libswresample",
                  ],
                  'defines': [
                    'NOMINMAX',
                    'WEBRTC_POSIX',
                  ],
                }],
              ],
            }],
            ['OS=="mac"', {
              'sources': [
                'exokit.cpp',
                '<!@(ls -1 deps/exokit-bindings/bindings/src/*.cc)',
                '<!@(ls -1 deps/exokit-bindings/util/src/*.cc)',
                '<!@(ls -1 deps/exokit-bindings/browser/src/*.cpp)',
                '<!@(ls -1 deps/exokit-bindings/canvas/src/*.cpp)',
                '<!@(ls -1 deps/exokit-bindings/nanosvg/src/*.cpp)',
                '<!@(ls -1 deps/exokit-bindings/canvascontext/src/*.cc)',
                '<!@(ls -1 deps/exokit-bindings/webglcontext/src/*.cc)',
                '<!@(ls -1 deps/exokit-bindings/webaudiocontext/src/*.cpp)',
                '<!@(ls -1 deps/exokit-bindings/videocontext/src/*.cpp)',
                '<!@(ls -1 deps/exokit-bindings/videocontext/src/mac/*.mm)',
                '<!@(ls -1 deps/exokit-bindings/windowsystem/src/*.cc)',
                '<!@(ls -1 deps/exokit-bindings/glfw/src/*.cc)',
                '<!@(ls -1 deps/exokit-bindings/webrtc/src/*.cc)',
                '<!@(ls -1 deps/openvr/src/*.cpp)',
              ],
              'include_dirs': [
                "<!(node -e \"console.log(require.resolve('nan').slice(0, -16))\")",
                "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/include')\")",
                "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/core')\")",
                "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/config')\")",
                "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/gpu')\")",
                "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/effects')\")",
                "<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/include')\")",
                "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/include')\")",
                "<!(node -e \"console.log(require.resolve('native-browser-deps').slice(0, -9) + '/lib')\")",
                "<!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/include')\")",
                "<!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/include/webrtc')\")",
                "<!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/headers')\")",
                '<(module_root_dir)/deps/exokit-bindings',
                '<(module_root_dir)/deps/exokit-bindings/utf8',
                '<(module_root_dir)/deps/exokit-bindings/node',
                '<(module_root_dir)/deps/exokit-bindings/native_app_glue',
                '<(module_root_dir)/deps/exokit-bindings/util/include',
                '<(module_root_dir)/deps/exokit-bindings/bindings/include',
                '<(module_root_dir)/deps/exokit-bindings/canvas/include',
                '<(module_root_dir)/deps/exokit-bindings/browser/include',
                '<(module_root_dir)/deps/exokit-bindings/nanosvg/include',
                '<(module_root_dir)/deps/exokit-bindings/canvascontext/include',
                '<(module_root_dir)/deps/exokit-bindings/webglcontext/include',
                '<(module_root_dir)/deps/exokit-bindings/webaudiocontext/include',
                '<(module_root_dir)/deps/exokit-bindings/videocontext/include',
                '<(module_root_dir)/deps/exokit-bindings/windowsystem/include',
                '<(module_root_dir)/deps/exokit-bindings/glfw/include',
                '<(module_root_dir)/deps/exokit-bindings/webrtc/include',
                '<(module_root_dir)/deps/openvr/include',
              ],
              'library_dirs': [
                "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/macos/glew')\")",
                "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/macos/glfw')\")",
                "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/lib/macos')\")",
                "<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/lib/macos')\")",
                "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/macos')\")",
                "<!(node -e \"console.log(require.resolve('native-browser-deps-macos').slice(0, -9) + '/lib3/macos')\")",
                "<!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/lib/macos')\")",
              ],
              'libraries': [
                '-framework OpenGL',
                '-framework Cocoa',
                '-lGLEW',
                '-lglfw3',
                '-lskia',
                '-framework CoreAudio',
                '-framework AVFoundation',
                '-framework AudioUnit',
                '-framework AudioToolbox',
                '-llabsound',
                '-lavformat.58',
                '-lavcodec.58',
                '-lavutil.56',
                '-lavdevice.58',
                '-lavfilter.7',
                '-lswscale.5',
                '-lswresample.3',
                '-lpostproc.55',
                '-lcef_dll_wrapper',
                "-F <!(node -e \"console.log(require.resolve('native-browser-deps-macos').slice(0, -9) + '/lib3/macos')\")",
                "-F <!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/lib/macos')\")",
                '-lwebrtc',
                "-framework 'Chromium Embedded Framework'",
                "-F <!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/bin/osx64')\")",
                "-framework OpenVR",
              ],
              'link_settings': {
                'libraries': [
                  "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/lib/macos')\")",
                  "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/macos')\")",
                  "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-browser-deps-macos').slice(0, -9) + '/lib3/macos')\")",
                  "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/lib/macos')\")",
                  "-framework 'Chromium Embedded Framework'",
                  "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/bin/osx64')\")",
                  '-framework OpenVR',
                ],
              },
              'copies': [
                {
                  'destination': '<(module_root_dir)/build/Release/',
                  'files': [
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/macos/libavformat.58.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/macos/libavcodec.58.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/macos/libavutil.56.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/macos/libavdevice.58.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/macos/libavfilter.7.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/macos/libswscale.5.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/macos/libswresample.3.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/macos/libpostproc.55.dylib')\")",
                  ]
                }
              ],
              'defines': [
                'OPENVR',
                'WRAPPING_CEF_SHARED',
                'WEBRTC_POSIX',
              ],
            }],
          ],
        }],
        ['"<!(echo $LUMIN)"=="1"', {
          'sources': [
            'exokit.cpp',
            '<!@(ls -1 deps/exokit-bindings/bindings/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/util/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/browser/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/canvas/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/nanosvg/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/canvascontext/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/webglcontext/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/webaudiocontext/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/videocontext/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/videocontext/src/linux/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/windowsystem/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/egl/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/webrtc/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/webrtc/src/converters/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/webrtc/src/webrtc/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/magicleap/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/magicleap/deps/sjpeg/src/*.cc)',
          ],
          'include_dirs': [
            "<!(node -e \"console.log(require.resolve('nan').slice(0, -16))\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/core')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/config')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/gpu')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/effects')\")",
            "<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/include')\")",
            "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/include')\")",
            "<!(node -e \"console.log(require.resolve('native-browser-deps').slice(0, -9) + '/lib')\")",
            "<!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/include')\")",
            "<!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/include/webrtc')\")",
            "<!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/include/webrtc/third_party/abseil-cpp')\")",
            "<!(node -e \"console.log(require.resolve('native-webrtc-deps').slice(0, -9) + '/include/webrtc/third_party/libyuv/include')\")",
            '<(module_root_dir)/deps/exokit-bindings',
            '<(module_root_dir)/deps/exokit-bindings/utf8',
            '<(module_root_dir)/deps/exokit-bindings/node',
            '<(module_root_dir)/deps/exokit-bindings/native_app_glue',
            '<(module_root_dir)/deps/exokit-bindings/util/include',
            '<(module_root_dir)/deps/exokit-bindings/bindings/include',
            '<(module_root_dir)/deps/exokit-bindings/canvas/include',
            '<(module_root_dir)/deps/exokit-bindings/browser/include',
            '<(module_root_dir)/deps/exokit-bindings/nanosvg/include',
            '<(module_root_dir)/deps/exokit-bindings/canvascontext/include',
            '<(module_root_dir)/deps/exokit-bindings/webglcontext/include',
            '<(module_root_dir)/deps/exokit-bindings/webaudiocontext/include',
            '<(module_root_dir)/deps/exokit-bindings/videocontext/include',
            '<(module_root_dir)/deps/exokit-bindings/windowsystem/include',
            '<(module_root_dir)/deps/exokit-bindings/egl/include',
            '<(module_root_dir)/deps/exokit-bindings/webrtc',
            '<(module_root_dir)/deps/exokit-bindings/magicleap/include',
            '<(module_root_dir)/deps/exokit-bindings/magicleap/deps/sjpeg/src',
            "<!(echo $MLSDK)/lumin/stl/libc++/include",
            "<!(echo $MLSDK)/lumin/usr/include",
            "<!(echo $MLSDK)/include",
          ],
          'library_dirs': [
            "<!(echo $MLSDK)/lumin/stl/libc++/lib",
            "<!(echo $MLSDK)/lumin/usr/lib",
            "<!(echo $MLSDK)/lib/lumin",
            "<(module_root_dir)/node_modules/native-canvas-deps/lib2/magicleap",
            "<(module_root_dir)/node_modules/native-audio-deps/lib2/magicleap",
            "<(module_root_dir)/node_modules/native-video-deps/lib2/magicleap",
            "<(module_root_dir)/node_modules/native-browser-deps-magicleap/lib5/magicleap",
            "<(module_root_dir)/node_modules/native-webrtc-deps/lib/magicleap",
          ],
          'libraries': [
            '-lskia',
            '-lLabSound',
            '-lavformat',
            '-lavcodec',
            '-lavutil',
            '-lavdevice',
            '-lswscale',
            '-lswresample',
            '-lopus',
            '-llog',
            '-lwebrtc',
          ],
          'ldflags': [
          ],
          'defines': [
            'NOMINMAX',
            'LUMIN',
            'WRAPPING_CEF_SHARED',
            'WEBRTC_POSIX',
          ],
        }],
      ],
    },
  ],
}
