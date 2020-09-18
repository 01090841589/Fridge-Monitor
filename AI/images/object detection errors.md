



### No module named 'nets'

1. PYTHONPATH가 올바른지 확인한다

   ``echo $PYTHONPATH`` 으로 research경로와 안의 slim이 제대로 들어가있는지 확인

   없으면 **research폴더에서**

   ```export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim```로 추가

   

2. 그래도 안되면

   ``python setup.py build``

   ``python setup.py install``

   

### tensorflow.python.framework.errors_impl.NotFoundError

1. 경로가 ``~``로 시작하는지 확인. ``./``로 교체
2. ``-``를``--``로 교체
3. 경로를 제대로 입력했는지 확인





### no module named pycocotools

coco받아서

1. Open `setup.py`
2. Remove the line `extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99'],`
3. Run`python setup.py build_ext install`