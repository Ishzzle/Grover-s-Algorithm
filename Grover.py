#!/usr/bin/env python
# coding: utf-8

# In[13]:


from qiskit import *
import matplotlib.pyplot as plt
from qiskit.tools.visualization import plot_histogram
import numpy as num
from qiskit import IBMQ
import math
pi = math.pi


# In[2]:


finder_q = QuantumRegister(4,'q')
finder_c = ClassicalRegister(4,'n')

finder = QuantumCircuit(finder_q, finder_c)
finder.x(0)
finder.x(1)
finder.x(2)
finder.x(3)

finder.draw()


# In[3]:


finder.cp(pi/4, 0, 3)
finder.cx(0, 1)
finder.cp(-pi/4, 1, 3)
finder.cx(0, 1)
finder.cp(pi/4, 1, 3)
finder.cx(1, 2)
finder.cp(-pi/4, 2, 3)
finder.cx(0, 2)
finder.cp(pi/4, 2, 3)
finder.cx(1, 2)
finder.cp(-pi/4, 2, 3)
finder.cx(0, 2)
finder.cp(pi/4, 2, 3)

#For 0000
#finder.x(0)
finder.x(1)
finder.x(2)
finder.x(3)

finder.to_gate
finder.draw()


# In[4]:


finder.h(0)
finder.h(1)
finder.h(2)
finder.h(3)
finder.x(0)
finder.x(1)
finder.x(2)
finder.x(3)

finder.cp(pi/4, 0, 3)
finder.cx(0, 1)
finder.cp(-pi/4, 1, 3)
finder.cx(0, 1)
finder.cp(pi/4, 1, 3)
finder.cx(1, 2)
finder.cp(-pi/4, 2, 3)
finder.cx(0, 2)
finder.cp(pi/4, 2, 3)
finder.cx(1, 2)
finder.cp(-pi/4, 2, 3)
finder.cx(0, 2)
finder.cp(pi/4, 2, 3)

finder.x(0)
finder.x(1)
finder.x(2)
finder.x(3)
finder.h(0)
finder.h(1)
finder.h(2)
finder.h(3)


# In[5]:


finder.barrier(finder_q)
finder.measure(0, 0)
finder.measure(1, 1)
finder.measure(2, 2)
finder.measure(3, 3)


# In[6]:


backend = Aer.get_backend('statevector_simulator')


# In[15]:


job = execute(finder, backend, shots=1024)
result = job.result().get_counts()
plot_histogram(result)


# In[10]:


#For IBM Simulator
IBMQ.load_account()
provider = provider = IBMQ.get_provider('ibm-q')
qcomp = provider.get_backend('ibmq_quito')
job = execute(finder, backend=qcomp)
from qiskit.tools.monitor import job_monitor
job_monitor(job)


# In[12]:


result = job.result()
plot_histogram(result.get_counts())


# In[ ]:




