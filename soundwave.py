# soundwave.py
# This file contains the SoundWave class that represents sounds in music.
import math 
import audio
class SoundWave:
  def __init__(self, halftones = 0, duration = 0.0, amp = 1.0, sample_rate = 44100):
    self.halftones = halftones
    self.duration = duration
    self.amp = amp
    self.sample_rate = sample_rate
    self.samples = []
    x = int(self.duration * self.sample_rate)
  
   
    freq =  220*(2**((self.halftones+3)/12))

    for t in range(x):
      s = self.amp * math.sin(2 * math.pi * freq * t/self.sample_rate)
      self.samples.append(s)
    

  def test_samples(self):
   
   
   for t in self.samples[0:10]:
     print(t)
   
  def save(self, filename):
    audio.save(filename, self.samples, self.sample_rate)

  def extend(self,s2):
    self.samples.extend(s2.samples)

  def __add__(self,s2):
    s = SoundWave()
    y =  min(len(self.samples),len(s2.samples))
    print(len(self.samples))
    print(len(s2.samples))
    #if len(self.samples) != len(s2.samples):
      #return s 
    for t in range(y):
      s.samples.append(self.samples[t] + s2.samples[t])
    if len(s2.samples) > len(self.samples):
      for c in range(y,len(s2.samples)):
       s.samples.append(s2.samples[c]) 
    if  len(s2.samples) < len(self.samples):
      for w in range(y,self.samples):
       s.samples.append(self.samples[w]) 
    return s
      
  
    

 
  
 


 

