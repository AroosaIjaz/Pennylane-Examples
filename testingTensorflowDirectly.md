

```python
import tensorflow as tf
```


```python
import pennylane as qml
from pennylane import numpy as np
```


```python
t1 = tf.get_variable("t1", [0, 0, 0], dtype=tf.float64)
t2 = tf.Variable([0, np.pi, 0], dtype=tf.float64)
```

    WARNING:tensorflow:From /home/moaraj/.local/lib/python3.6/site-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
    Instructions for updating:
    Colocations handled automatically by placer.


    20:56:06 WARNING From /home/moaraj/.local/lib/python3.6/site-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
    Instructions for updating:
    Colocations handled automatically by placer.



```python
t1
```




    <tf.Variable 't1:0' shape=(0, 0, 0) dtype=float64_ref>




```python
graph1 = tf.Graph()
with graph1.as_default():
    init = tf.global_variables_initializer()
with tf.Session(graph = graph1) as sess:
    sess.run(init)

```


```python
graph2 = tf.Graph()
with graph2.as_default():
    dev = qml.device('default.qubit', wires=3)
    @qml.qnode(dev, interface='tf')
    def circuit(p1, p2):
        qml.Rot(p1[0],p1[1],p1[2], wires =1)
        qml.Rot(p2[0],p2[1],p2[2], wires =2)
        return qml.expval.PauliZ(0), qml.expval.PauliZ(1), qml.expval.PauliZ(2)
```


```python
with tf.Session(graph = graph2) as sess:
    result = sess.run(circuit(t1,t2))
    print(result)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-8-1d2c1aac6ecd> in <module>
          1 with tf.Session(graph = graph2) as sess:
    ----> 2     result = sess.run(circuit(t1,t2))
          3     print(result)


    ~/.local/lib/python3.6/site-packages/pennylane/decorator.py in wrapper(*args, **kwargs)
        151         def wrapper(*args, **kwargs):
        152             """Wrapper function"""
    --> 153             return qnode(*args, **kwargs)
        154 
        155         # bind the jacobian method to the wrapped function


    ~/.local/lib/python3.6/site-packages/pennylane/qnode.py in __call__(self, *args, **kwargs)
        455         # pylint: disable=no-member
        456         args = autograd.builtins.tuple(args)  # prevents autograd boxed arguments from going through to evaluate
    --> 457         return self.evaluate(args, **kwargs)  # args as one tuple
        458 
        459     @ae.primitive


    ~/.local/lib/python3.6/site-packages/autograd/tracer.py in f_wrapped(*args, **kwargs)
         46             return new_box(ans, trace, node)
         47         else:
    ---> 48             return f_raw(*args, **kwargs)
         49     f_wrapped.fun = f_raw
         50     f_wrapped._is_autograd_primitive = True


    ~/.local/lib/python3.6/site-packages/pennylane/qnode.py in evaluate(self, args, **kwargs)
        469         if not self.ops:
        470             # construct the circuit
    --> 471             self.construct(args, **kwargs)
        472 
        473         # temporarily store keyword arguments


    ~/.local/lib/python3.6/site-packages/pennylane/qnode.py in construct(self, args, **kwargs)
        268 
        269         # flatten the args, replace each with a Variable instance with a unique index
    --> 270         temp = [Variable(idx) for idx, val in enumerate(_flatten(args))]
        271         self.num_variables = len(temp)
        272 


    ~/.local/lib/python3.6/site-packages/pennylane/qnode.py in <listcomp>(.0)
        268 
        269         # flatten the args, replace each with a Variable instance with a unique index
    --> 270         temp = [Variable(idx) for idx, val in enumerate(_flatten(args))]
        271         self.num_variables = len(temp)
        272 


    ~/.local/lib/python3.6/site-packages/pennylane/utils.py in _flatten(x)
         59     elif isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
         60         for item in x:
    ---> 61             yield from _flatten(item)
         62     else:
         63         yield x


    ~/.local/lib/python3.6/site-packages/pennylane/utils.py in _flatten(x)
         58         yield from _flatten(x.flat)  # should we allow object arrays? or just "yield from x.flat"?
         59     elif isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
    ---> 60         for item in x:
         61             yield from _flatten(item)
         62     else:


    ~/.local/lib/python3.6/site-packages/tensorflow/python/ops/variables.py in __iter__(self)
        948       TypeError: when invoked.
        949     """
    --> 950     raise TypeError("'Variable' object is not iterable.")
        951 
        952   # NOTE(mrry): This enables the Variable's overloaded "right" binary


    TypeError: 'Variable' object is not iterable.



```python

```


```python

```
