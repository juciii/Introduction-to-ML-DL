docker run -e -t -v $HOME:$HOME \
    -e ko_KR.UTF-8 \
    -e PYTHONIOENCODING=utf_8 \
    ubuntu-phantomjs /bin/bash