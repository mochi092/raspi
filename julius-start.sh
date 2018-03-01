#!/bin/sh

julius -C ~/julius-4.4.2.1/kit/dictation-kit-v4.4/word.jconf -module > /dev/null &
echo $! #プロセスIDを出力
sleep 2 #2秒間スリープ
