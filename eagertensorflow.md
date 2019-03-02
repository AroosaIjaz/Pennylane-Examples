

```python
import tensorflow as tf
import tensorflow.contrib.eager as tfe
tf.enable_eager_execution()
```


```python
#check if eager mode is working
tfe.executing_eagerly()
```




    True




```python
#get version of tf in ypur computer
tf.__version__
```




    '1.13.1'




```python
#test the eager execution
x = [[2.]]
m = tf.matmul(x, x)
print("hello, {}".format(m))
```

    hello, [[4.]]



```python
import pennylane as qml
from pennylane import numpy as np
```


```python
#define circuit and qnode
dev2 = qml.device('default.qubit', wires=3)

@qml.qnode(dev2, interface='tfe')
def circuit2(p1, p2):
    qml.Rot(p1[0],p1[1],p1[2], wires =1)
    qml.Rot(p2[0],p2[1],p2[2], wires =2)
    return qml.expval.PauliZ(0), qml.expval.PauliZ(1), qml.expval.PauliZ(2)
```


    ---------------------------------------------------------------------------

    QuantumFunctionError                      Traceback (most recent call last)

    <ipython-input-12-503cfda54275> in <module>
          2 dev2 = qml.device('default.qubit', wires=3)
          3 
    ----> 4 @qml.qnode(dev2, interface='tfe')
          5 def circuit2(p1, p2):
          6     qml.Rot(p1[0],p1[1],p1[2], wires =1)


    ~/.local/lib/python3.6/site-packages/pennylane/decorator.py in qfunc_decorator(func)
        146 
        147         if interface == 'tfe':
    --> 148             return qnode.to_tfe()
        149 
        150         @wraps(func)


    ~/.local/lib/python3.6/site-packages/pennylane/qnode.py in to_tfe(self)
        808         except ImportError: # pragma: no cover
        809             raise QuantumFunctionError("TensorFlow with eager execution mode not found. Please install "
    --> 810                                        "the latest version of TensorFlow to enable the TFEQNode interface.") from None
        811 
        812         return TFEQNode(self)


    QuantumFunctionError: TensorFlow with eager execution mode not found. Please install the latest version of TensorFlow to enable the TFEQNode interface.



```python
t1 = tfe.Variable([0, np.pi, 0], dtype=tf.float64)
t2 = tfe.Variable([0, np.pi, 0], dtype=tf.float64)
```


```python
t1
```




    <tf.Variable 'Variable:0' shape=(3,) dtype=float64, numpy=array([0.        , 3.14159265, 0.        ])>




```python
opt = tf.train.GradientDescentOptimizer(learning_rate=0.1)
```


```python
#using J=[1,-1] as default couplings
def cost(var):
#       J= tf.constant([1, -1])
        spins=circuit2(var[0],var[1])
        energy=-(1*spins[0]*spins[1])-(-1*spins[1]*spins[2])
        return energy
loss= cost([t1,t2])
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-16-4d8710f3c82a> in <module>
          5         energy=-(1*spins[0]*spins[1])-(-1*spins[1]*spins[2])
          6         return energy
    ----> 7 loss= cost([t1,t2])
    

    <ipython-input-16-4d8710f3c82a> in cost(var)
          2 def cost(var):
          3 #       J= tf.constant([1, -1])
    ----> 4         spins=circuit2(var[0],var[1])
          5         energy=-(1*spins[0]*spins[1])-(-1*spins[1]*spins[2])
          6         return energy


    NameError: name 'circuit2' is not defined



```python
opt = tf.train.GradientDescentOptimizer(learning_rate=0.1)
```


```python
train = opt.minimize(loss)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-18-dcafb77b7151> in <module>
    ----> 1 train = opt.minimize(loss)
    

    NameError: name 'loss' is not defined



```python

```
